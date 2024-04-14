import chainlit as cl
import pandas as pd
import numpy as np
from agents.query_agent import Query_Agent
from agents.general_agent import General_Agent
import os

hashcode = np.random.randint(0, 1000000)


async def Query_bot(query: str) -> str:
    chat_agent = Query_Agent()
    res = chat_agent.run(query=query)
    return res

async def generic_bot(query: str) -> str:
    general_agent = General_Agent()
    res =general_agent.run(query=query)
    return res

@cl.step(type="chatbot")
async def chatbot_step(query: str):
    # Simulate a running task
    response = await generic_bot(query)
    return response

@cl.step(type="Querybot")
async def Querybot_step(query: str, response: str):
    # Simulate a running task
    response = await Query_bot(query)
    return response

@cl.on_message
async def main(message: cl.Message):
    # Draw Info from conversation.
    global hashcode
    # Check if Chatlog/hashcode.txt exists
    if not os.path.exists(f"Chatlog/{hashcode}.txt"):
        # Create the file if it doesn't exist
        with open(f"Chatlog/{hashcode}.txt", "w") as file:
            pass
    else:
        # Read the contents of the file
        with open(f"Chatlog/{hashcode}.txt", "r") as file:
            chat_history = file.read()
    # Append message.content to the file
    with open(f"Chatlog/{hashcode}.txt", "a") as file:
        file.write(f"Q: {message.content}\n")
    # Chatbot Goes here
    chainlit_message = await chatbot_step(f"Q:{message.content}")
    if "Redirect_Code:#1821" in chainlit_message:
        chainlit_message = await Querybot_step(message.content, chainlit_message)
    # Append chainlit_message to the file
    with open(f"Chatlog/{hashcode}.txt", "a") as file:
        file.write(f"A: {chainlit_message}\n")
    # Send Back to user
    await cl.Message(content=chainlit_message).send()