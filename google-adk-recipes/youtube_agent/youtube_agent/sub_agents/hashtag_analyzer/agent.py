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

"""hashtag_analyzer_agent: for analyzing trending hashtags and optimizing social media reach"""

from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-pro" 

hashtag_analyzer_agent = LlmAgent(
    model=MODEL,
    name="hashtag_analyzer_agent",
    instruction=prompt.HASHTAG_ANALYZER_PROMPT,
    output_key="hashtag_analyzer_output",
)
