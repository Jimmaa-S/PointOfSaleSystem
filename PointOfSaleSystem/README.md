PointOfSaleSystem
Overview

The PointOfSaleSystem is a console-based Python application designed for supermarket-type stores. It allows cashiers to log in, process sales, handle returns, update inventory, and generate receipts. This system also supports backroom operations such as inventory reports and daily sales reports.

Features

User Authentication

Cashiers log in using a user ID and password.

Maximum of 3 failed login attempts; locks user on failure.

Sales Operations

Start new sale and add/remove items.

Calculate running totals, generate unique receipt IDs (UUID), and save receipts to file.

Returns

Single item return.

Full sale return.

Inventory Management

Load items from RetailStoreItemData.txt.

Update item quantities after sales/returns.

Backroom Operations

Inventory report: current stock and threshold.

Daily sales report: total sales per transaction.