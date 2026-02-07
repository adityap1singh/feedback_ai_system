class QualityCriticAgent:
    def review(self, ticket):
        required = ["ticket_id", "category", "priority"]
        return all(k in ticket for k in required)