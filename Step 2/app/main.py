import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Declaring the FASTAPI app
app = FastAPI()

# Choosing the apporiate pipleine and model
unmasker = pipeline("fill-mask", model="bert-base-uncased")


# Defining request data model
class Input(BaseModel):
    input: str


# Posting the request to predict route
@app.post("/predict")
async def prediction(model_input: Input):
    input = model_input.input
    result = unmasker(input)
    return result


# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info", reload=True)
