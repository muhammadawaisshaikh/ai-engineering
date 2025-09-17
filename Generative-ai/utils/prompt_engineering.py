def create_prompt_template(template_type="creative_writing"):
    """
    Create prompt templates for different use cases
    
    Args:
        template_type (str): Type of prompt template
    
    Returns:
        str: Prompt template
    """
    templates = {
        "creative_writing": "Write a {genre} story about {topic} with the following elements: {elements}",
        "technical_explanation": "Explain {concept} in {audience} terms. Include examples related to {domain}",
        "code_generation": "Write a {language} function that {task}. The function should {requirements}",
        "image_generation": "{style} of {subject} in {setting}, {details}, {color_scheme} color scheme",
        "business_email": "Write a {tone} email to {recipient} about {topic}. Key points to include: {points}"
    }
    
    return templates.get(template_type, "{input}")

def enhance_prompt(base_prompt, style=None, length=None, perspective=None):
    """
    Enhance a basic prompt with additional specifications
    
    Args:
        base_prompt (str): The original prompt
        style (str): Writing or artistic style
        length (str): Desired length or detail level
        perspective (str): Point of view or perspective
    
    Returns:
        str: Enhanced prompt
    """
    enhanced = base_prompt
    
    if style:
        enhanced += f" in the style of {style}"
    
    if length:
        enhanced += f". Make it {length}"
    
    if perspective:
        enhanced += f" from the perspective of {perspective}"
    
    return enhanced

def generate_example_prompts(category, num_examples=3):
    """
    Generate example prompts for different categories
    
    Args:
        category (str): Category of prompts
        num_examples (int): Number of examples to generate
    
    Returns:
        list: List of example prompts
    """
    examples = {
        "creative": [
            "A short story about a robot who discovers emotions",
            "A poem about the changing seasons in a cyberpunk city",
            "A dialogue between two AI systems discussing humanity"
        ],
        "technical": [
            "Explain quantum computing to a 10-year-old",
            "Compare and contrast machine learning and deep learning",
            "Describe how neural networks work using analogies"
        ],
        "visual": [
            "A futuristic cityscape at sunset, digital art",
            "An astronaut riding a horse on Mars, photorealistic",
            "A cute robot playing guitar in a garden, cartoon style"
        ],
        "code": [
            "Python function to calculate Fibonacci sequence",
            "JavaScript code for a responsive navigation menu",
            "SQL query to find the top 5 customers by revenue"
        ]
    }
    
    return examples.get(category, [])[:num_examples]

if __name__ == "__main__":
    # Example usage
    template = create_prompt_template("creative_writing")
    prompt = template.format(genre="science fiction", topic="time travel", elements="paradox, adventure, emotional conflict")
    print("Template:", template)
    print("Generated prompt:", prompt)
    
    enhanced = enhance_prompt("Explain artificial intelligence", style="simple terms", length="brief", perspective="a educator")
    print("Enhanced prompt:", enhanced)
    
    print("\nExample creative prompts:")
    for example in generate_example_prompts("creative"):
        print(f"- {example}")
