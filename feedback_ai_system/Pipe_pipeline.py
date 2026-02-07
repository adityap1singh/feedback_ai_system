import openai
import os
from dotenv import load_dotenv
from bug_agent import BugAnalysisAgent
from classifier_agent import ClassifierAgent
from create_agent import Agent, CreateAgent
from csv_reader_agent import CSVReaderAgent
from feature_agent import FeatureAgent
from quality_agent import QualityAgent
from ticket_agent import TicketAgent


def main():
    print("🚀 Pipeline started")

    csv_agent = CSVReaderAgent()
    bug_agent = BugAgent()
    classifier = ClassifierAgent()
    feature_agent = FeatureAgent()
    quality_agent = QualityAgent()
    ticket_agent = TicketAgent()
    creator = CreateAgent()

    data = csv_agent.run("data.csv")
    data = bug_agent.run(data)
    data = classifier.run(data)
    data = feature_agent.run(data)
    data = quality_agent.run(data)
    result = creator.run(data)
    ticket_agent.run(result)

    print("✅ Pipeline completed")


if __name__ == "__main__":
    main()

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_pipeline(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content