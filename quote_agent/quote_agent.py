
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

def create_quote_agent() -> LlmAgent:
    """Constructs the ADK agent."""
    return LlmAgent(
        model="gemini-2.0-flash-001",
        name="quote_agent",
        description="An agent that can help questions about getting a quote from Einstein",
        instruction="""You are a specialized Einstein quote retrieval assistant. Your primary function is to return a famous quote from Einstein and no one else.""",
    )
