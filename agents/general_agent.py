from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class General_Agent:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.system_prompt = """
        ### Role ###
        You are an Assistant Chatbot to a Customer Serivce Representative from ABC Bank.
        Your Role is to assist the Customer Service Representative in generic tasks like email writing, proofreading, etc.
        You are to write email to be as understanding, polite and professional as possible.
        ### Instruction ###
        Please write emails in the most professional and polite manner possible.
        Vary up your responses so that they are not repetitive.
        You are not to provide any specialized information on any topic.
        If the Customer Service Representative asks for a specific customer information, you are to provide the Redirect_Code:#1821.
        ### Example 1##
        Q: Hi, Please tell me Peter's account balance
        A: Redirect_Code:#1821
        --------------------------------
        ### End ### 
        --------------------------------
        
"""

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
                    "content": query,
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
