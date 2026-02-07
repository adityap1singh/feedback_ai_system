import uuid

class TicketCreatorAgent:
    def create_ticket(self, source_id, category, priority, details):
        return {
            "ticket_id": str(uuid.uuid4())[:8],
            "source_id": source_id,
            "category": category,
            "priority": priority,
            "details": str(details),
            "status": "Open"
        }