from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Initialize FastAPI app
app = FastAPI()

# Load the fine-tuned model and tokenizer
model_name = "Risha6h/Llama-3.2-3B-Instructunsloth-merged"  # Updated model name

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.to("cuda" if torch.cuda.is_available() else "cpu")

# Define request body
class InferenceRequest(BaseModel):
    prompt: str
    max_length: int = 200
    temperature: float = 0.7

def generate_text(prompt: str, max_length: int, temperature: float):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    output = model.generate(
        **inputs,
        max_new_tokens=max_length,
        temperature=temperature
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

@app.post("/generate")
def infer(request: InferenceRequest):
    response_text = generate_text(request.prompt, request.max_length, request.temperature)
    return {"response": response_text}

# Run the app using: uvicorn filename:app --reload
