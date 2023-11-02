from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(temperature = 0.1)

def csv_reader(filepath,user_question ):
    agent = create_csv_agent(llm, filepath, verbose = True)
    if user_question is not None and user_question != "":
        response = agent.run(user_question)
        return response

