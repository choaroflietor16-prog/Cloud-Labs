# Drink Credit System

A Flask prototype for assigning event drink credits and redeeming them through a QR-assisted lookup. `app.py` handles guest and scanner requests, `templates/` renders the interface and `static/css/` provides styling. Guest balance and redemption log entries are in memory and reset on restart.

| Workflow | Routes |
| --- | --- |
| Guest list and guest changes | `/`, `/guests/add`, `/guests/edit/<gid>`, `/guests/delete/<gid>` |
| QR generation | `/qr/<gid>` returns a PNG that encodes the guest ID. |
| Redemption | `/scanner`, POST `/scanner/lookup`, `/scanner/deduct/<gid>` |
| History | `/log` |

From this folder, create and activate a virtual environment and run `python -m pip install -r requirements.txt`. Start with `python -m flask --app app run --host 127.0.0.1 --port 5001` and open `http://127.0.0.1:5001/`. Create a synthetic guest, generate the QR, look up the guest, deduct a credit, and compare the remaining balance with the log. Check insufficient credits and unknown guest IDs as well. Browser camera availability depends on browser permissions and the page security context.

The QR carries a lookup identifier. The server owns the balance. Future work includes persistent storage, operator authentication, protected POST mutations and transactional redemption.
