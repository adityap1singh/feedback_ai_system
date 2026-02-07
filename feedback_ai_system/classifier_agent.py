class FeedbackClassifierAgent:
    def classify(self, text):
        text = text.lower()
        if any(k in text for k in ["crash", "error", "not working", "login"]):
            return "Bug", "High"
        if any(k in text for k in ["add", "feature", "please"]):
            return "Feature Request", "Medium"
        if any(k in text for k in ["love", "amazing", "great"]):
            return "Praise", "Low"
        if "buy" in text or "www" in text:
            return "Spam", "Low"
        return "Complaint", "Low"

class ClassifierAgent:
    def run(self, data):
        print("🏷️ Classifier Agent running")
        data["classified"] = True
        return data