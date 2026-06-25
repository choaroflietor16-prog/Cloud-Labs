from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import qrcode
import io
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = "drink_secret_key_2024"

# ── In-memory guest list ───────────────────────────────────────────────
guests = [
    {"id": "G001", "name": "Sipho Khumalo",  "credits": 5, "used": 0, "created": "2024-06-01"},
    {"id": "G002", "name": "Priya Naidoo",   "credits": 3, "used": 0, "created": "2024-06-01"},
    {"id": "G003", "name": "James van Wyk",  "credits": 8, "used": 0, "created": "2024-06-01"},
]

log = []

def find_guest(gid):
    return next((g for g in guests if g["id"] == gid), None)

def next_guest_id():
    if not guests:
        return "G001"
    nums = []
    for g in guests:
        try:
            nums.append(int(g["id"][1:]))
        except:
            pass
    return f"G{(max(nums) + 1):03d}" if nums else "G001"

# ── Admin: guest list ──────────────────────────────────────────────────
@app.route("/")
def guests_list():
    return render_template("guests.html", guests=guests, active="guests")

# ── Admin: add guest ───────────────────────────────────────────────────
@app.route("/guests/add", methods=["GET", "POST"])
def guest_add():
    if request.method == "POST":
        name    = request.form.get("name", "").strip()
        credits = request.form.get("credits", "0")
        if not name:
            flash("Guest name is required.", "error")
            return redirect(url_for("guest_add"))
        try:
            credits = int(credits)
        except:
            credits = 0
        guests.append({
            "id":      next_guest_id(),
            "name":    name,
            "credits": credits,
            "used":    0,
            "created": datetime.now().strftime("%Y-%m-%d"),
        })
        flash(f"Guest '{name}' added.", "success")
        return redirect(url_for("guests_list"))
    return render_template("guest_form.html", guest=None, active="guests")

# ── Admin: edit guest ──────────────────────────────────────────────────
@app.route("/guests/edit/<gid>", methods=["GET", "POST"])
def guest_edit(gid):
    g = find_guest(gid)
    if not g:
        flash("Guest not found.", "error")
        return redirect(url_for("guests_list"))
    if request.method == "POST":
        g["name"]    = request.form.get("name", g["name"]).strip()
        try:
            g["credits"] = int(request.form.get("credits", g["credits"]))
        except:
            pass
        flash("Guest updated.", "success")
        return redirect(url_for("guests_list"))
    return render_template("guest_form.html", guest=g, active="guests")

# ── Admin: delete guest ────────────────────────────────────────────────
@app.route("/guests/delete/<gid>")
def guest_delete(gid):
    global guests
    guests = [g for g in guests if g["id"] != gid]
    flash("Guest removed.", "success")
    return redirect(url_for("guests_list"))

# ── QR code image ──────────────────────────────────────────────────────
@app.route("/qr/<gid>")
def qr_code(gid):
    g = find_guest(gid)
    if not g:
        return "Guest not found", 404
    img = qrcode.make(gid)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

# ── Scanner: lookup guest by ID ────────────────────────────────────────
@app.route("/scanner")
def scanner():
    return render_template("scanner.html", active="scanner", guest=None, scanned=False)

@app.route("/scanner/lookup", methods=["POST"])
def scanner_lookup():
    gid = request.form.get("guest_id", "").strip().upper()
    g   = find_guest(gid)
    if not g:
        flash("Guest not found.", "error")
        return render_template("scanner.html", active="scanner", guest=None, scanned=True)
    return render_template("scanner.html", active="scanner", guest=g, scanned=True)

# ── Scanner: deduct one credit ─────────────────────────────────────────
@app.route("/scanner/deduct/<gid>")
def deduct(gid):
    g = find_guest(gid)
    if not g:
        flash("Guest not found.", "error")
        return redirect(url_for("scanner"))
    if g["credits"] <= 0:
        flash("No credits remaining.", "error")
        return render_template("scanner.html", active="scanner", guest=g, scanned=True)
    g["credits"] -= 1
    g["used"]    += 1
    log.append({
        "guest_id":   gid,
        "guest_name": g["name"],
        "time":       datetime.now().strftime("%H:%M:%S"),
        "date":       datetime.now().strftime("%Y-%m-%d"),
        "credits_left": g["credits"],
    })
    flash(f"1 credit deducted. {g['credits']} remaining.", "success")
    return render_template("scanner.html", active="scanner", guest=g, scanned=True)

# ── Log page ───────────────────────────────────────────────────────────
@app.route("/log")
def view_log():
    return render_template("log.html", log=list(reversed(log)), active="log")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)