from flask import *
import sqlite3


def get_db():  # return database
    db = sqlite3.connect('jpcafev2.db')
    return db

app = Flask(__name__)


@app.route('/')
def home(error=""):
    connection = get_db()
    data = connection.execute('SELECT * FROM Inventory').fetchall()
    return render_template('orderpage.html', data=data, potential_err_msg=error)


@app.route('/register')
def register(error=""):
    return render_template('register.html', potential_err_msg=error)


@app.route('/registered', methods=['POST'])
def registered():
    data = request.form
         
    name = data["membername"]
    email = data["member_email"]
    pw = data["memberpassword"] 

    connection = get_db()

    with connection: 
        if connection.execute('''SELECT COUNT(*) FROM Member 
        WHERE mem_name = ?''', (name, )).fetchone()[0] > 0:
            return register("User already exists!")
        
        connection.execute("INSERT INTO Member VALUES (?, ?, ?)", (name, email, pw))

    
    return render_template('registered.html')


@app.route('/ordered', methods=['POST'])
def ordered():

    connection = get_db() 

    data = request.form

    button_clicked = data["button_press"]

    isMember = False 

    # determine if user is member 
    if button_clicked == "Member login and Order":
        email = data["member_email"]
        pw = data["memberpassword"]
        memberData = connection.execute('''SELECT mem_name, password 
        FROM Member 
        WHERE email = ?''', (email, )).fetchone()
       
        if memberData == None:
            return home("Invalid Username!")
        
        passwordFromDB = memberData[1]
        name = memberData[0]
        if pw == passwordFromDB:
            isMember = True 
        else: 
            return home("Wrong Password!")
    else: 
        name = data["customer_name"]

    quantityArr = data.getlist("quantity")

    displayArr = [] 

    for i in range(0, len(quantityArr)): 
        
        currQtyOrdered = quantityArr[i]
        item_id = i + 1 

        if currQtyOrdered != "": 
            if currQtyOrdered.lstrip('-').isdigit() == False:
                return home("Please only enter integers into quantity boxes!")
            quantityOrder = int(currQtyOrdered)
            
            if quantityOrder < 0: # negative
                return home("A quantity ordered is negative! Only positive quantities please!")
            
            if quantityOrder > 0: # we are actl orderng this item 
                currItemData = connection.execute('''SELECT item_name, price, available_quantity
                FROM Inventory
                WHERE item_id = ?''', (item_id, )).fetchone()
                if currItemData[2] < int(currQtyOrdered):
                    return home("Insufficient quantity for %s, only %d available." % (currItemData[0], currItemData[2]))
                
                # all pass, we are ordering this item 
                displayArr.append(currItemData)

                connection.execute('''UPDATE Inventory
                SET available_quantity = ?
                WHERE item_id = ?''', (currItemData[2]-quantityOrder, item_id))
                connection.commit()
    
    return render_template('ordered.html', name=name, displayArr=displayArr)


if __name__ == '__main__':
    app.run()
