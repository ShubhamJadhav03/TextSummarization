from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os

from src.textSummarizer.pipeline.predicition_pipeline import PredictionPipeline

app = FastAPI()

# Load templates from "templates" folder
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["root"])
async def index():
    # Redirect to Swagger docs by default
    return RedirectResponse(url="/docs")

# Route to render frontend UI
@app.get("/ui", response_class=HTMLResponse)
async def ui_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Training route
@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return {"message": "Training successful !!"}
    except Exception as e:
        return {"error": str(e)}

# Prediction API (backend)
@app.post("/predict")
async def predict_route(text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        output = obj.predict(text)
        return {"summary": output}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

