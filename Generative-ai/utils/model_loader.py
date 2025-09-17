from transformers import pipeline, AutoModel, AutoTokenizer
from diffusers import StableDiffusionPipeline, DiffusionPipeline
import torch
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_text_generation_model(model_name="gpt2", device=None):
    """
    Load a text generation model
    
    Args:
        model_name (str): Name or path of the model
        device (str): Device to load the model on
    
    Returns:
        pipeline: Text generation pipeline
    """
    if device is None:
        device = 0 if torch.cuda.is_available() else -1
    
    logger.info(f"Loading text generation model: {model_name}")
    
    try:
        generator = pipeline(
            "text-generation",
            model=model_name,
            device=device,
            torch_dtype=torch.float16 if device == 0 else torch.float32
        )
        return generator
    except Exception as e:
        logger.error(f"Error loading model {model_name}: {e}")
        raise

def load_diffusion_model(model_id="runwayml/stable-diffusion-v1-5", device=None):
    """
    Load a diffusion model for image generation
    
    Args:
        model_id (str): Model identifier from Hugging Face Hub
        device (str): Device to load the model on
    
    Returns:
        pipeline: Diffusion pipeline
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    logger.info(f"Loading diffusion model: {model_id}")
    
    try:
        if device == "cuda":
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float16,
                safety_checker=None,
                requires_safety_checker=False
            )
        else:
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                safety_checker=None,
                requires_safety_checker=False
            )
        
        pipe = pipe.to(device)
        return pipe
    except Exception as e:
        logger.error(f"Error loading diffusion model {model_id}: {e}")
        raise

def load_model_for_task(task, model_name, **kwargs):
    """
    Generic model loader for different tasks
    
    Args:
        task (str): Type of task (text-generation, text-to-image, etc.)
        model_name (str): Name or path of the model
    
    Returns:
        object: Loaded model or pipeline
    """
    task_loaders = {
        "text-generation": load_text_generation_model,
        "text-to-image": load_diffusion_model,
        # Add more task loaders as needed
    }
    
    if task not in task_loaders:
        raise ValueError(f"Unsupported task: {task}. Available tasks: {list(task_loaders.keys())}")
    
    return task_loaders[task](model_name, **kwargs)
