 Point of Sale (POS) System – Python Console Application

Technologies: Python, File I/O, OOP, UUID, CSV, Git/GitHub
Concepts: Object-Oriented Programming, Authentication, Inventory Management, Sales Processing

 Project Overview

This project is a console-based Point of Sale (POS) system designed to simulate real-world retail operations. The application authenticates users, manages inventory, processes sales and returns, generates receipts, and supports backroom reporting operations. The system emphasizes clean architecture, modular design, and Python fundamentals.

 User Authentication

Secure login using User ID and Password

Maximum 3 login attempts before lockout

Role-based access (Cashier / Admin)

Credentials loaded from an external file

 Inventory Management

Inventory data loaded from RetailStoreItemData.txt

Items stored using a dictionary keyed by UPC

Tracks:

Item description

Unit price

Quantity on hand

Reorder threshold

Automatically updates inventory after sales and returns

 Sales & Transactions

Start a new sale and add/remove items by UPC

Real-time running total calculation

Finalize sale with payment processing

Each sale generates a unique receipt ID using UUID

Receipts include:

Items purchased

Quantities

Total amount

Sales history stored for returns and reporting

 Returns Processing

Supports:

Single-item returns

Full sale returns

Inventory is restored automatically after returns

Return amount calculated accurately based on quantities returned

 Backroom Operations & Reports

Inventory report showing:

Item name

Current stock

Reorder threshold

Daily sales summary

Monthly sales aggregation

Receipts saved to files for auditing

 System Design

Modular project structure

Separation of concerns:

Models (Item, Sale, Inventory)

Services (Receipts, Reports)

Security (Authentication)

Easily extensible for:

SQLite database integration

Web-based UI (FastAPI)

Tax and discount rules

 Why This Project Matters

This project demonstrates:

Strong Python fundamentals

Practical use of OOP principles

Real-world retail system logic

Clean code organization

Version control using Git & GitHub
