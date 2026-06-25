CREATE TABLE nav_history (
    id INTEGER PRIMARY KEY,
    scheme_name TEXT,
    nav REAL,
    nav_date DATE
);

CREATE TABLE investor_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_name TEXT,
    amount REAL,
    transaction_date DATE
);