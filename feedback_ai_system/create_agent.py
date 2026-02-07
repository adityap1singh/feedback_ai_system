# agents/create_agent.py
from openai import OpenAI

class Agent:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.client = OpenAI()  # Make sure OPENAI_API_KEY is set in env

    def run(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content