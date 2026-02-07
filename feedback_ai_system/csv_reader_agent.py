# agents/csv_reader_agent.py
from openai import OpenAI

class CSVReaderAgent:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.client = OpenAI()

    def ask(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def run(self, file_path):
        print("📄 CSV Reader Agent running")
        return {"raw_data": "sample"}