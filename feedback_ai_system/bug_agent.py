class BugAnalysisAgent:
    def analyze(self, text):
        return {
            "steps": "User reports issue during normal usage",
            "severity": "Critical" if "crash" in text.lower() else "High"
        }