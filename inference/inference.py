from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize the FastAPI app
app = FastAPI()

# Initialize the text-generation pipeline with the correct model identifier
text_generator = pipeline("text-generation", model="gpt2")

# Define the request body using Pydantic
class TextGenerationRequest(BaseModel):
    input_text: str
    max_length: int = 50  # Optional parameter to set maximum text length

# Define the response model
class TextGenerationResponse(BaseModel):
    generated_text: str

# Create an endpoint for text generation
@app.post("/generate-text", response_model=TextGenerationResponse)
async def generate_text(request: TextGenerationRequest):
    generated = text_generator(request.input_text, max_length=request.max_length)
    return TextGenerationResponse(generated_text=generated[0]['generated_text'])