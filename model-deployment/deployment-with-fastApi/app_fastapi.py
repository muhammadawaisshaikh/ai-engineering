from fastapi import FastAPI
from pydantic import BaseModel
from save_load import load_model

app = FastAPI()
model = load_model()

class Features(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Features):
    prediction = model.predict([data.features]).tolist()
    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)