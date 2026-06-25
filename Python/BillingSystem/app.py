from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = "billing_secret_key_2024"

customers = [
    {"id": "c1", "name": "Sipho Khumalo",  "email": "sipho@example.com",  "phone": "082 111 2233", "created": "2024-01-10"},
    {"id": "c2", "name": "Priya Naidoo",   "email": "priya@example.com",   "phone": "071 444 5566", "created": "2024-02-14"},
    {"id": "c3", "name": "James van Wyk",  "email": "james@example.com",   "phone": "063 777 8899", "created": "2024-03-01"},
]

invoices = [
    {"id": "INV-001", "customer_id": "c1", "customer_name": "Sipho Khumalo", "amount": 1500.00, "status": "Paid",    "date": "2024-04-01", "due": "2024-04-15", "description": "Web design services"},
    {"id": "INV-002", "customer_id": "c2", "customer_name": "Priya Naidoo",  "amount": 3200.00, "status": "Pending", "date": "2024-04-10", "due": "2024-04-24", "description": "Monthly retainer"},
    {"id": "INV-003", "customer_id": "c3", "customer_name": "James van Wyk", "amount":  850.00, "status": "Overdue", "date": "2024-03-20", "due": "2024-04-03", "description": "Consulting"},
]

def get_stats():
    return {
        "total_revenue":   sum(i["amount"] for i in invoices if i["status"] == "Paid"),
        "pending_amt":     sum(i["amount"] for i in invoices if i["status"] == "Pending"),
        "total_customers": len(customers),
        "total_invoices":  len(invoices),
        "overdue_count":   sum(1 for i in invoices if i["status"] == "Overdue"),
        "paid_count":      sum(1 for i in invoices if i["status"] == "Paid"),
        "pending_count":   sum(1 for i in invoices if i["status"] == "Pending"),
    }

def find_customer(cid):
    return next((c for c in customers if c["id"] == cid), None)

def find_invoice(iid):
    return next((i for i in invoices if i["id"] == iid), None)

def next_invoice_id():
    if not invoices:
        return "INV-001"
    nums = []
    for inv in invoices:
        try:
            nums.append(int(inv["id"].split("-")[1]))
        except:
            pass
    return f"INV-{(max(nums) + 1):03d}" if nums else "INV-001"

@app.route("/")
def dashboard():
    recent = sorted(invoices, key=lambda x: x["date"], reverse=True)[:5]
    return render_template("dashboard.html", stats=get_stats(), recent=recent, active="dashboard")

@app.route("/customers")
def customers_list():
    return render_template("customers.html", customers=customers, active="customers")

@app.route("/customers/add", methods=["GET", "POST"])
def customer_add():
    if request.method == "POST":
        name  = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        if not name:
            flash("Customer name is required.", "error")
            return redirect(url_for("customer_add"))
        customers.append({
            "id":      "c" + str(uuid.uuid4())[:6],
            "name":    name,
            "email":   email,
            "phone":   phone,
            "created": datetime.now().strftime("%Y-%m-%d"),
        })
        flash(f"Customer '{name}' added.", "success")
        return redirect(url_for("customers_list"))
    return render_template("customer_form.html", customer=None, active="customers")

@app.route("/customers/edit/<cid>", methods=["GET", "POST"])
def customer_edit(cid):
    c = find_customer(cid)
    if not c:
        flash("Customer not found.", "error")
        return redirect(url_for("customers_list"))
    if request.method == "POST":
        c["name"]  = request.form.get("name",  c["name"]).strip()
        c["email"] = request.form.get("email", c["email"]).strip()
        c["phone"] = request.form.get("phone", c["phone"]).strip()
        flash("Customer updated.", "success")
        return redirect(url_for("customers_list"))
    return render_template("customer_form.html", customer=c, active="customers")

@app.route("/customers/delete/<cid>")
def customer_delete(cid):
    global customers
    customers = [c for c in customers if c["id"] != cid]
    flash("Customer removed.", "success")
    return redirect(url_for("customers_list"))

@app.route("/invoices")
def invoices_list():
    status_filter = request.args.get("status", "All")
    filtered = invoices if status_filter == "All" else [i for i in invoices if i["status"] == status_filter]
    return render_template("invoices.html", invoices=filtered, status_filter=status_filter, active="invoices")

@app.route("/invoices/add", methods=["GET", "POST"])
def invoice_add():
    if request.method == "POST":
        cid  = request.form.get("customer_id", "")
        desc = request.form.get("description", "").strip()
        amt  = request.form.get("amount", "0")
        due  = request.form.get("due", "")
        try:
            amount = float(amt)
        except:
            flash("Invalid amount.", "error")
            return redirect(url_for("invoice_add"))
        c = find_customer(cid)
        if not c:
            flash("Select a valid customer.", "error")
            return redirect(url_for("invoice_add"))
        invoices.append({
            "id":            next_invoice_id(),
            "customer_id":   cid,
            "customer_name": c["name"],
            "amount":        amount,
            "status":        "Pending",
            "date":          datetime.now().strftime("%Y-%m-%d"),
            "due":           due,
            "description":   desc,
        })
        flash("Invoice created.", "success")
        return redirect(url_for("invoices_list"))
    return render_template("invoice_form.html", invoice=None, customers=customers, active="invoices")

@app.route("/invoices/edit/<iid>", methods=["GET", "POST"])
def invoice_edit(iid):
    inv = find_invoice(iid)
    if not inv:
        flash("Invoice not found.", "error")
        return redirect(url_for("invoices_list"))
    if request.method == "POST":
        inv["description"] = request.form.get("description", inv["description"]).strip()
        inv["due"]         = request.form.get("due",    inv["due"])
        inv["status"]      = request.form.get("status", inv["status"])
        try:
            inv["amount"] = float(request.form.get("amount", inv["amount"]))
        except:
            pass
        flash("Invoice updated.", "success")
        return redirect(url_for("invoices_list"))
    return render_template("invoice_form.html", invoice=inv, customers=customers, active="invoices")

@app.route("/invoices/delete/<iid>")
def invoice_delete(iid):
    global invoices
    invoices = [i for i in invoices if i["id"] != iid]
    flash("Invoice deleted.", "success")
    return redirect(url_for("invoices_list"))

@app.route("/invoices/mark/<iid>/<status>")
def invoice_mark(iid, status):
    inv = find_invoice(iid)
    if inv and status in ("Paid", "Pending", "Overdue"):
        inv["status"] = status
        flash(f"Invoice marked as {status}.", "success")
    return redirect(url_for("invoices_list"))

@app.route("/invoices/view/<iid>")
def invoice_view(iid):
    inv = find_invoice(iid)
    if not inv:
        flash("Invoice not found.", "error")
        return redirect(url_for("invoices_list"))
    return render_template("invoice_view.html", inv=inv, active="invoices")

@app.route("/history")
def history():
    paid = sorted([i for i in invoices if i["status"] == "Paid"], key=lambda x: x["date"], reverse=True)
    return render_template("history.html", invoices=paid, active="history")

settings_data = {
    "business_name":  "My Business",
    "business_email": "billing@mybusiness.co.za",
    "currency":       "R",
    "tax_rate":       15,
    "payment_terms":  14,
    "footer_note":    "Thank you for your business.",
}

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        settings_data["business_name"]  = request.form.get("business_name",  "").strip()
        settings_data["business_email"] = request.form.get("business_email", "").strip()
        settings_data["currency"]       = request.form.get("currency", "R").strip()
        try:
            settings_data["tax_rate"]      = float(request.form.get("tax_rate", 15))
            settings_data["payment_terms"] = int(request.form.get("payment_terms", 14))
        except:
            pass
        settings_data["footer_note"] = request.form.get("footer_note", "").strip()
        flash("Settings saved.", "success")
        return redirect(url_for("settings"))
    return render_template("settings.html", s=settings_data, active="settings")

if __name__ == "__main__":
    app.run(debug=True)