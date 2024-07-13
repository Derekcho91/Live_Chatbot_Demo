# ChatBot Demo
### Brief
Hello, and welcome to the Chatbot demo that my organization didn't want me to present.
So a little bit of background, On last Friday (12/04/2024), I was asked to do a Chatbot for a POC/Demo to my department on possible utilizations of LLMs.
After rushing it over the weekend, I presented it to my manager and the department head, who decided not to present it for unknown reasons.
To not let the effort go to waste, I decided to put it up on github after I removed all the PII. Please take a look.

### Implementation
It is actually a simple implementation of using LangChain libraries and Chainlit as a front end. I used Langchain to build a vector store with my company's FAQ Website. Also integrated Tavily for more general searches.

### To-Do/Future Improvements
1. Function for PDF Vector Search. Tried using the Langchain Library Function but it does not seem to be returning the right vectors. Might have to use a custom function for this.
2. Long Term Chat History Function. Don't want to spend money on storage so might just end up using a Log Folder. My organization has access to Azure Databricks so might try that.
3. Claude Intergation. Seems to be the best out of the bunch but Langchain support is limited.
4. Azure Copilot Intergation. I don't really like the model to be honest but Microsoft's relationship with us is like Oracle's


### How to run
1. Create a .env file in the root directory with your OPENAI_API_KEY and TAVILY_API_KEY like shown below
    ```
    OPENAI_API_KEY=XXXX
    TAVILY_API_KEY=XXX
    ```
2. Create a conda or virtual environment if required and run below commands
    ```
    pip install -r requirements.txt
    chainlit run main.py -w
    ```
