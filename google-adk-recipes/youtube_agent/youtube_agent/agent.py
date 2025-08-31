# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""YouTube Agent assists in researching trending video topics and creating viral social media content."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.trending_research import trending_research_agent
from .sub_agents.social_media_creator import social_media_creator_agent
from .sub_agents.hashtag_analyzer import hashtag_analyzer_agent

MODEL = "gemini-2.5-pro" 

youtube_agent = LlmAgent(
    name="youtube_agent",
    model=MODEL,
    description=(
        "Research trending YouTube video topics and create viral social media posts "
        "with market-trending hashtags. Analyze current video trends, identify viral "
        "content patterns, and generate engaging social media content that capitalizes "
        "on trending topics and hashtags for maximum reach and engagement."
    ),
    instruction=prompt.YOUTUBE_AGENT_PROMPT,
    tools=[
        AgentTool(agent=trending_research_agent),
        AgentTool(agent=social_media_creator_agent),
        AgentTool(agent=hashtag_analyzer_agent),
    ],
)

root_agent = youtube_agent
