import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

def generate_image(prompt, model_id="runwayml/stable-diffusion-v1-5", output_path="generated_image.png"):
    """
    Generate an image from text prompt using Stable Diffusion
    
    Args:
        prompt (str): Text description of the desired image
        model_id (str): Model identifier from Hugging Face Hub
        output_path (str): Path to save the generated image
    
    Returns:
        PIL.Image: Generated image
    """
    # Check if CUDA is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    
    # Load the pipeline
    print(f"Loading model {model_id} on {device}...")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=dtype,
        safety_checker=None,  # Disable safety checker for demonstration
        requires_safety_checker=False
    )
    pipe = pipe.to(device)
    
    # Generate image
    print(f"Generating image for prompt: '{prompt}'")
    with torch.autocast(device):
        image = pipe(prompt, guidance_scale=7.5, num_inference_steps=50).images[0]
    
    # Save image
    image.save(output_path)
    print(f"Image saved to {output_path}")
    
    return image

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    # Example prompts
    prompts = [
        "a futuristic cityscape at sunset, digital art, highly detailed",
        "an astronaut riding a horse on Mars, photorealistic",
        "a cute robot playing guitar in a garden, cartoon style"
    ]
    
    # Generate images for each prompt
    for i, prompt in enumerate(prompts):
        output_path = f"outputs/generated_image_{i+1}.png"
        generate_image(prompt, output_path=output_path)
