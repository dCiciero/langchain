from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily_client = TavilyClient()


@tool
def search(query: str):
    """
    Tool that searches the internet for the given query.

    Args:
        query (str): The search query.

    Returns:
        str: The search results.
    """
    # Implement the search functionality here
    print(f"Search results for query: {query}")
    return tavily_client.search(query=query)


llm = ChatOpenAI(model="gpt-5")
tools = [search]

agent = create_agent(model=llm, tools=tools)


def main() -> None:
    print("Hello from langchain-course!")
    # Example usage of the agent
    response = agent.invoke({"messages":[HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(response)

if __name__ == "__main__":
    main()
