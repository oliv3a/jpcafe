# JP Cafe ☕🍣

A simple Japanese cafe ordering website built with **Flask** (a Python web framework) and **SQLite** (a lightweight database stored in a single file).

Customers can browse the menu, order as a guest, or register as a member and log in to order.

## Features

- 🍱 **Menu page**: shows every item from the inventory with its image, description, price and stock
- 🧾 **Ordering**: order as a guest (just enter a name) or log in as a member
- 👤 **Member registration**: sign up with a name, email and password
- ✅ **Input checks**: rejects non-numbers, negative quantities, and orders bigger than the stock left
- 📦 **Stock tracking**: available quantity goes down automatically after each order

## Tech Stack

| Part      | Tool                  |
|-----------|-----------------------|
| Backend   | Python + Flask        |
| Database  | SQLite (`jpcafev2.db`) |
| Frontend  | HTML (Jinja templates) + CSS |

## Project Structure

```
jpcafe/
├── flaskk.py            # Main Flask app (all the routes)
├── populateDB.py        # Script that fills the database from the data files
├── jpcafev2.db          # SQLite database
├── jpcafev2.sqbpro      # DB Browser for SQLite project file
├── inventory.csv / .txt # Menu items: id, name, description, price, quantity, image
├── member.csv / .txt    # Sample members
├── transactionlog.csv / .txt  # Sample order history
├── static/              # Food images, logo, styles.css
└── templates/           # HTML pages
    ├── orderpage.html   # Home / menu page
    ├── register.html    # Sign-up form
    ├── registered.html  # Sign-up success page
    └── ordered.html     # Order confirmation page
```

## Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/oliv3a/jpcafe.git
   cd jpcafe
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the app**
   ```bash
   python flaskk.py
   ```

4. Open **http://127.0.0.1:5000** in your browser.

The database (`jpcafev2.db`) already has data in it, so you don't need to run `populateDB.py` unless you're rebuilding it from scratch.

## Routes

| Route         | Method | What it does |
|---------------|--------|--------------|
| `/`           | GET    | Shows the menu and order form |
| `/register`   | GET    | Shows the sign-up form |
| `/registered` | POST   | Saves a new member |
| `/ordered`    | POST   | Checks the order, updates stock, shows confirmation |

## Notes

- This is a **school project**. All member and transaction data is made-up sample data.
- Passwords are stored as **plain text**, which is fine for learning but not safe for a real app. A real app would hash them first (scramble them one-way, e.g. with `werkzeug.security`).

## Possible Improvements

- Hash member passwords
- Save each order to a transaction table
- Calculate the total, member discount and total payable in `/ordered` (`ordered.html` already has spots for them, but the app doesn't send the values yet)
