from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import json
import csv

load_dotenv()  # take environment variables from .env.

def load_database(file_path: str) -> str:
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    json_string = json.dumps(data)
    return json_string

class Query_Agent:
    

    

    def __init__(self) -> None:
        self.client = OpenAI()
        self.system_prompt = """
        ### Role ###
        You are an Assistant Chatbot to a Customer Serivce Representative from ABC Bank.
        Your Role is to assist the Customer Service Representative in answering the customer's queries.
        
        ### Instruction ###
        Provide the Customer Service Representative with the information that is requested by the Customer, like Account Balance, Transaction History, etc.
        Do Not Provide any information to the Customer Service Representative that is not related to the Bank's Services.
        Limit yourself to only the information avaliable in the Database.
        ### Example 1###
        Customer Service Representative: "What is my Account Balance?"
        Assistant Chatbot: "Your Account Balance is $18182."
        ### Example 2###
        Customer Service Representative: "Please provide the transaction history of my account."
        Assistant Chatbot: "Your Transaction History is as follows:..."
        ### Example 3###
        Customer Service Representative: "What is the weather today?"
        Assistant Chatbot: "I am sorry, I cannot provide you with that information."
        ### End ###
        -------------------------------
        
"""
        self.json_string = f"Please Search in this Database:({load_database('Dummy_Dataset.csv')})"

    def run(self, query: str) -> str:

        result = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": query+" "+self.json_string
                },
            ],
            temperature= 0.1,
            max_tokens=150,
            top_p=1
        )
        return result.choices[0].message.content

    def run2(self, problem) -> str:
        print("Inside Chatbot ", problem)
        return "Chatbot"
