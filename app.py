from fastapi import FastAPI, Form, Request
import uvicorn
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return JSONResponse(
            content={
                "status": "completed",
                "message": "Training completed successfully!",
            }
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status": "error",
                "message": f"Error occurred during training: {e}",
            }
        )


@app.get("/summarizer", response_class=HTMLResponse)
async def summarizer_page(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "summary": None}
    )


@app.post("/summarizer", response_class=HTMLResponse)
async def summarizer(request: Request, text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        print(f"Generated summary: {summary}")
        return templates.TemplateResponse(
            "index.html", {"request": request, "summary": summary}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html", {"request": request, "summary": f"Error: {e}"}
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
