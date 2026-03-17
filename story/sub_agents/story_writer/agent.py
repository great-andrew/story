from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .models import StoryWriterOutput
from .prompt import CONTENT_PLANNER_DESCRIPTION, CONTENT_PLANNER_PROMPT

MODEL = LiteLlm("openai/gpt-4o")

story_writer_agent = Agent(
    name="StoryWriterAgent",
    model=MODEL,
    output_key="story",
    output_schema=StoryWriterOutput,
    description=CONTENT_PLANNER_DESCRIPTION,
    instruction=CONTENT_PLANNER_PROMPT,
)
