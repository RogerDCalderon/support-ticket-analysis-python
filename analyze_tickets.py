tickets = [
    {"id": 1, "status": "open", "priority": "high"},
    {"id": 2, "status": "closed", "priority": "low"},
    {"id": 3, "status": "open", "priority": "medium"},
]

open_tickets = [t for t in tickets if t["status"] == "open"]

print("Open tickets:")
for t in open_tickets:
    print(f"Ticket {t['id']} - Priority: {t['priority']}")
