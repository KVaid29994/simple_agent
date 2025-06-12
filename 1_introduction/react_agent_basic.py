from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults

from dotenv import load_dotenv

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

search_tool = TavilySearchResults(search_depth = "basic")

tools = [search_tool]

agent = initialize_agent(tools = tools, llm = model, agent="zero-shot-react-description", verbose = True)
agent.invoke("Make me a tweet about weather in delhi today, where ypu tell the temprature in day, night and evening with emojis")

