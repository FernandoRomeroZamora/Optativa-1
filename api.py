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
async def menu(request: Request):
    return templates.TemplateResponse("presentacion.html", {"request": request})

# Ruta para la gráfica 1
@app.get("/grafica1")
async def grafica1(request: Request):
    return templates.TemplateResponse("grafica1.html", {"request": request})

# Ruta para la gráfica 2
@app.get("/grafica2")
async def grafica2(request: Request):
    return templates.TemplateResponse("grafica2.html", {"request": request})

# Ruta para la gráfica 3
@app.get("/grafica3")
async def grafica3(request: Request):
    return templates.TemplateResponse("grafica3.html", {"request": request})

# Ruta para la gráfica 4
@app.get("/grafica4")
async def grafica4(request: Request):
    return templates.TemplateResponse("grafica4.html", {"request": request})

# Ruta para la gráfica 5
@app.get("/grafica5")
async def grafica5(request: Request):
    return templates.TemplateResponse("grafica5.html", {"request": request})

# Ruta para la gráfica 6
@app.get("/grafica6")
async def grafica6(request: Request):
    return templates.TemplateResponse("grafica6.html", {"request": request})

# Ruta para la gráfica 7
@app.get("/grafica7")
async def grafica7(request: Request):
    return templates.TemplateResponse("grafica7.html", {"request": request})

# Ruta para la gráfica 8
@app.get("/grafica8")
async def grafica8(request: Request):
    # Leer el archivo CSV desde la carpeta 'static'
    csv_path = os.path.join(static_path, "CarrosUsados.csv")
    lectura = pd.read_csv(csv_path)

    # Generar la gráfica del kilometraje promedio por año
    mileage_avg = lectura.groupby("Year")["Mileage"].mean().reset_index()
    fig2 = px.bar(
        mileage_avg,
        x="Year",
        y="Mileage",
        title="Kilometraje Promedio de Vehículos por Año de Fabricación",
        labels={"Year": "Año", "Mileage": "Kilometraje (kmpl)"},
        color="Mileage",
        color_continuous_scale="Viridis"
    )

    # Convertir la gráfica a JSON
    graph_json = fig2.to_json()

    # Pasar el JSON a la plantilla
    return templates.TemplateResponse("grafica8.html", {"request": request, "graph_json": graph_json})


# Ruta para la gráfica 9
@app.get("/grafica9")
async def grafica9(request: Request):
    csv_path = os.path.join(static_path, "CarrosUsados.csv")
    lectura = pd.read_csv(csv_path)

    data_avg = lectura.groupby(["Year", "Fuel_Type"])["Price"].mean().reset_index()
    fig = px.line(
        data_avg,
        x="Year",
        y="Price",
        color="Fuel_Type",
        title="Evolución del Precio Medio por Año y Tipo de Combustible",
        labels={"Year": "Año", "Price": "Precio Medio", "Fuel_Type": "Tipo de Combustible"}
    )

    graph_json = fig.to_json()

    return templates.TemplateResponse("grafica9.html", {"request": request, "graph_json": graph_json})


# Ruta para la gráfica 10 - Distribución de Potencia por Tipo de Transmisión
@app.get("/grafica10")
async def grafica10(request: Request):
    csv_path = os.path.join(static_path, "CarrosUsados.csv")
    lectura = pd.read_csv(csv_path)

    fig = px.violin(
        lectura,
        x="Transmission",
        y="Power",
        color="Transmission",
        title="Distribución de Potencia por Tipo de Transmisión",
        labels={"Transmission": "Tipo de Transmisión", "Power": "Potencia (bhp)"},
        box=True,
        points="all"
    )

    graph_json = fig.to_json()

    return templates.TemplateResponse("grafica10.html", {"request": request, "graph_json": graph_json})


# Ruta para la gráfica 11 - Relación entre Año de Fabricación y Kilometraje según Transmisión
@app.get("/grafica11")
async def grafica11(request: Request):
    csv_path = os.path.join(static_path, "CarrosUsados.csv")
    lectura = pd.read_csv(csv_path)

    fig = px.scatter(
        lectura,
        x="Year",
        y="Mileage",
        color="Transmission",
        title="Relación entre Año de Fabricación y Kilometraje según Transmisión",
        labels={"Year": "Año", "Mileage": "Kilometraje (kmpl)", "Transmission": "Tipo de Transmisión"},
        size="Price",
        hover_data=["Fuel_Type"]
    )

    graph_json = fig.to_json()

    return templates.TemplateResponse("grafica11.html", {"request": request, "graph_json": graph_json})


# Página de presentación del proyecto
@app.get("/presentacion", response_class=HTMLResponse)
async def presentacion(request: Request):
    return templates.TemplateResponse("presentacion.html", {"request": request})

# Página principal con el menú (las gráficas)
@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})