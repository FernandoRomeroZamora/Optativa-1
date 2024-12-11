from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
import os
import pandas as pd
import plotly.express as px

app = FastAPI()

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Plantillas
templates = Jinja2Templates(directory="templates")

# Página principal con el menú
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para la gráfica 2
@app.get("/histograma")
async def histograma(request: Request):
    return templates.TemplateResponse("histograma.html", {"request": request})

# Ruta para la gráfica 3
@app.get("/grafica_violin")
async def grafica_violin(request: Request):
    return templates.TemplateResponse("grafica_violin.html", {"request": request})

# Ruta para la gráfica 4
@app.get("/grafica_pastel")
async def grafica_pastel(request: Request):
    return templates.TemplateResponse("/grafica_pastel.html", {"request": request})

# Ruta para la gráfica 5
@app.get("/grafica_dispersion2")
async def grafica_dispersion2(request: Request):
    return templates.TemplateResponse("grafica_dispersion2.html", {"request": request})

# Ruta para la gráfica 6
@app.get("/grafica_dispersion")
async def grafica6(request: Request):
    return templates.TemplateResponse("grafica_dispersion.html", {"request": request})

# Ruta para la gráfica 7
@app.get("/grafica_barras")
async def grafica_barras(request: Request):
    return templates.TemplateResponse("grafica_barras.html", {"request": request})