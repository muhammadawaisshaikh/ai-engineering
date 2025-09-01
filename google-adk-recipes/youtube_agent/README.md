# YouTube Agent - AI-Powered Trending Research & Viral Content Creation

An intelligent AI agent built with Google Agent Development Kit (ADK) that researches trending YouTube video topics and creates viral social media posts with market-trending hashtags.

## Features

### Trending Research Agent
- **Real-time Trend Analysis**: Identifies current trending YouTube topics and viral content patterns
- **Viral Content Patterns**: Analyzes what makes content go viral in specific niches
- **Audience Insights**: Provides engagement patterns and viewer behavior analysis
- **Content Opportunities**: Identifies gaps and unique angles in trending topics
- **Competitive Analysis**: Analyzes top-performing creators and content strategies

### Hashtag Analyzer Agent
- **Trending Hashtag Identification**: Finds high-performing hashtags for maximum reach
- **Platform Optimization**: Provides platform-specific hashtag strategies
- **Performance Analysis**: Analyzes hashtag reach potential and competition levels
- **Strategic Combinations**: Creates optimal hashtag sets and rotation strategies
- **Competitive Insights**: Analyzes competitor hashtag strategies

### Social Media Creator Agent
- **Viral Content Generation**: Creates multiple post variations optimized for viral potential
- **Platform-Specific Content**: Generates content tailored for Instagram, TikTok, Twitter, LinkedIn
- **Hashtag Integration**: Strategically incorporates trending hashtags throughout content
- **Engagement Optimization**: Includes elements that drive comments, shares, and saves
- **A/B Testing**: Provides content variations for testing different approaches

## Architecture

The YouTube Agent follows a modular architecture with three specialized subagents, each implemented as a `LlmAgent` from Google ADK:

```
youtube_agent/
├── youtube_agent/
│   ├── __init__.py              # Package initialization
│   ├── agent.py                 # Main coordinator agent (LlmAgent)
│   ├── prompt.py                # Main agent instructions
│   └── sub_agents/
│       ├── trending_research/   # YouTube trend analysis
│       │   ├── __init__.py      # Exports trending_research_agent
│       │   ├── agent.py         # Trending research LlmAgent
│       │   └── prompt.py        # Trending research instructions
│       ├── hashtag_analyzer/    # Hashtag strategy optimization
│       │   ├── __init__.py      # Exports hashtag_analyzer_agent
│       │   ├── agent.py         # Hashtag analyzer LlmAgent
│       │   └── prompt.py        # Hashtag analysis instructions
│       └── social_media_creator/ # Viral content generation
│           ├── __init__.py      # Exports social_media_creator_agent
│           ├── agent.py         # Social media creator LlmAgent
│           └── prompt.py        # Content creation instructions
├── pyproject.toml               # Poetry configuration with dependencies
├── requirements.txt             # Pip dependencies
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.9+
- Google Cloud Platform account
- Google ADK access

### Setup Instructions

1. **Create a Python virtual environment:**
   ```sh
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - On Windows (CMD):
     ```sh
     .venv\Scripts\activate.bat
     ```
   - On Windows (PowerShell):
     ```sh
     .venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

3. **Install Google ADK:**
   ```sh
   pip install google-adk
   ```

4. **Start the ADK API server with CORS enabled:**
   ```sh
   adk api_server --allow_origins="*" --reload --reload_agents 
   ```
   
   **Alternative: Allow all origins (less secure but easier for development):**
   ```sh
   adk api_server --allow_origins="*" --reload --reload_agents 
   ```

5. **Start the ADK WEB Interface:**
   ```sh
   adk web --allow_origins="*" --reload --reload_agents 
   ```

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd youtube_agent
```

2. **Install dependencies using Poetry (recommended)**
```bash
poetry install
```

**Or using pip:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables .env**
```bash
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

4. **Run the agent using Google ADK CLI**
```bash
# Using Poetry
poetry run adk run youtube_agent

# Using pip
adk web --allow_origins="*"
```

## Implementation Details

### Agent Architecture
- **Main Agent**: `youtube_agent` - A `LlmAgent` that coordinates all subagents
- **Subagents**: Each subagent is implemented as a `LlmAgent` with specialized prompts
- **Tool Integration**: Uses `AgentTool` to integrate subagents as tools for the main agent
- **Model**: All agents use Gemini 2.5 Pro by default

### Code Structure
```python
# Main agent (youtube_agent/agent.py)
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

youtube_agent = LlmAgent(
    name="youtube_agent",
    model="gemini-2.5-pro",
    tools=[
        AgentTool(agent=trending_research_agent),
        AgentTool(agent=social_media_creator_agent),
        AgentTool(agent=hashtag_analyzer_agent),
    ],
)

# Subagent example (sub_agents/trending_research/agent.py)
from google.adk.agents import LlmAgent

trending_research_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="trending_research_agent",
    instruction=prompt.TRENDING_RESEARCH_PROMPT,
    output_key="trending_research_output",
)
```

### Dependencies
The project uses Poetry for dependency management with the following key packages:
- `google-adk>=1.0.0` - Google Agent Development Kit
- `google-genai>=1.9.0` - Google Generative AI
- `google-cloud-aiplatform[adk,agent-engines]>=1.93.0` - Google Cloud AI Platform
- `pydantic>=2.10.6` - Data validation
- `python-dotenv>=1.0.1` - Environment variable management

## Usage

### Basic Workflow

1. **Start the YouTube Agent using ADK**
   ```bash
   adk run youtube_agent
   ```

2. **Research Trending Topics**
   - The trending research agent analyzes current YouTube trends
   - Identifies viral content opportunities in your niche
   - Provides actionable insights and recommendations

3. **Analyze Trending Hashtags**
   - The hashtag analyzer identifies high-performing hashtags
   - Creates platform-specific hashtag strategies
   - Optimizes for maximum reach and engagement

4. **Create Viral Social Media Content**
   - The social media creator generates multiple post variations
   - Optimizes content for different platforms
   - Incorporates trending hashtags strategically

### Example Interaction

```
User: "I want to create content about tech reviews and my target audience is young professionals interested in the latest gadgets."

YouTube Agent: "I'll help you research trending tech review topics and create viral social media content. Let me start by analyzing current YouTube trends in the tech review space."

[trending_research tool reports: Analysis complete - Top trending topics include AI gadgets, foldable phones, and sustainable tech with high viral potential]

YouTube Agent: "Great! I found some exciting trending topics. Now let me analyze the best hashtags for maximum reach."

[hashtag_analyzer tool reports: Hashtag strategy created - #TechReview, #GadgetReview, #AI, #Innovation trending with 2M+ reach]

YouTube Agent: "Perfect! Now let me create viral social media posts incorporating these trending topics and hashtags."

[social_media_creator tool reports: Content package generated - 5 Instagram posts, 3 TikTok scripts, and 2 Twitter threads ready]
```

## Use Cases

### Content Creators
- Research trending topics in your niche
- Create viral social media content
- Optimize hashtag strategies for maximum reach
- Stay ahead of content trends

### Marketing Teams
- Identify viral content opportunities
- Create engaging social media campaigns
- Optimize content for different platforms
- Leverage trending hashtags for brand awareness

### Social Media Managers
- Generate platform-specific content
- Optimize posting strategies
- Analyze trending topics and hashtags
- Create engaging, shareable content

## Configuration

### Model Selection
The agent uses Gemini 2.5 Pro by default. You can modify the model in each agent file:

```python
MODEL = "gemini-2.5-pro"  # Change to your preferred model
```

### Custom Prompts
Each subagent has customizable prompts in their respective `prompt.py` files. Modify these to tailor the agent's behavior to your specific needs.

## Development

### Project Structure
- **Poetry-based**: Uses Poetry for dependency management and project configuration
- **Modular Design**: Each subagent is self-contained with its own prompts and logic
- **ADK Integration**: Built specifically for Google ADK framework
- **Type Safety**: Uses Pydantic for data validation

### Testing
The project includes development dependencies for testing:
```bash
poetry install --with dev
poetry run pytest
```

### Code Quality
Development tools include:
- `black` for code formatting
- `pytest` for testing
- `pytest-asyncio` for async testing support

## Performance Metrics

The YouTube Agent is designed to optimize for:
- **Viral Potential**: Content designed to maximize shares and engagement
- **Reach Optimization**: Strategic hashtag usage for maximum visibility
- **Platform Performance**: Content optimized for each social media platform
- **Trend Relevance**: Content that capitalizes on current viral topics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Google Agent Development Kit (ADK)
- Powered by Google's Gemini AI models
- Designed for maximum viral content potential

## Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Contact the development team
- Check the documentation for common solutions

---

**Transform your social media presence with AI-powered trending research and viral content creation!**
