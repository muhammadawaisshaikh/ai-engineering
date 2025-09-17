from transformers import pipeline, set_seed
import torch

def generate_text(prompt, model_name="gpt2", max_length=50, num_return_sequences=1):
    """
    Generate text using a pre-trained language model
    
    Args:
        prompt (str): Input text to complete
        model_name (str): Name of the pre-trained model
        max_length (int): Maximum length of generated text
        num_return_sequences (int): Number of sequences to generate
    
    Returns:
        list: Generated text sequences
    """
    # Set seed for reproducibility
    set_seed(42)
    
    # Create text generation pipeline
    generator = pipeline("text-generation", 
                        model=model_name, 
                        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                        device=0 if torch.cuda.is_available() else -1)
    
    # Generate text
    completions = generator(
        prompt, 
        max_length=max_length, 
        num_return_sequences=num_return_sequences,
        temperature=0.7,
        do_sample=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    
    return [completion['generated_text'] for completion in completions]

if __name__ == "__main__":
    # Example usage
    prompt = "The future of AI is"
    
    print("Generating text with GPT-2...")
    results = generate_text(prompt, model_name="gpt2", max_length=50, num_return_sequences=2)
    
    for i, result in enumerate(results):
        print(f"\nResult {i+1}:")
        print(result)
    
    # Example with different model
    print("\n" + "="*50)
    print("Generating text with distilgpt2...")
    results_distil = generate_text(prompt, model_name="distilgpt2", max_length=50, num_return_sequences=1)
    print(results_distil[0])
