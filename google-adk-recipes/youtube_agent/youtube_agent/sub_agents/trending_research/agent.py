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

"""trending_research_agent: for analyzing YouTube trends and viral content patterns"""

from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-pro" 

trending_research_agent = LlmAgent(
    model=MODEL,
    name="trending_research_agent",
    instruction=prompt.TRENDING_RESEARCH_PROMPT,
    output_key="trending_research_output",
)
