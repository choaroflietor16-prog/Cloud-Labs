# Billing System

A Flask prototype for managing customers and tracking invoices from creation through payment. `app.py` owns the routes and data, `templates/` contains Jinja views, and `static/css/` supplies styling. Customers, invoices and settings live in Python collections and reset on restart.

| Workflow | Routes |
| --- | --- |
| Overview | `/` |
| Customers | `/customers`, `/customers/add`, `/customers/edit/<cid>`, `/customers/delete/<cid>` |
| Invoices | `/invoices`, `/invoices/add`, `/invoices/edit/<iid>`, `/invoices/view/<iid>`, `/invoices/mark/<iid>/<status>`, `/invoices/delete/<iid>` |
| Paid history and settings | `/history`, `/settings` |

From this folder, create a virtual environment, activate it and install Flask with `python -m pip install -r requirements.txt`. Run `python -m flask --app app run --host 127.0.0.1 --port 5000` and open `http://127.0.0.1:5000/`. Use synthetic names and amounts. Add a customer, create and view an invoice, change its status and check paid history. A restart should reset changes.

The in-memory design makes the workflow easy to demonstrate. Future work includes persistent storage, authenticated access, CSRF-protected POST mutations and a session key loaded from the environment.
