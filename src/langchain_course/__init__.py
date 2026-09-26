from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# tavily_client = TavilyClient()


# @tool
# def search(query: str):
#     """
#     Tool that searches the internet for the given query.

#     Args:
#         query (str): The search query.

#     Returns:
#         str: The search results.
#     """
#     # Implement the search functionality here
#     print(f"Search results for query: {query}")
#     return tavily_client.search(query=query)


class Source(BaseModel):
    """Schema for a source used by the agent"""
    # name: str = Field(..., description="The name of the source")
    url: str = Field(..., description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent's response"""
    answer: str = Field(..., description="The content of the agent's response")
    sources: List[Source] = Field(default_factory=list, description="The sources used by the agent")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]

agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main() -> None:
    print("Hello from langchain-course!")
    # Example usage of the agent
    response = agent.invoke({"messages":[HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(response)

if __name__ == "__main__":
    main()
