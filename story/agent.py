from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .prompt import STORY_PRODUCER_DESCRIPTION, STORY_PRODUCER_INSTRUCTION
from google.adk.models.lite_llm import LiteLlm
from .sub_agents.story_writer.agent import story_writer_agent
from .sub_agents.illustrator.agent import illustrator_agent

MODEL = LiteLlm(model="openai/gpt-4o")

story_producer_agent = Agent(
    name="StoryProducerAgent",
    model=MODEL,
    description=STORY_PRODUCER_DESCRIPTION,
    instruction=STORY_PRODUCER_INSTRUCTION,
    tools=[
        AgentTool(agent=story_writer_agent),
        AgentTool(agent=illustrator_agent),
    ],
)

root_agent = story_producer_agent
