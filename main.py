from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()
load_dotenv()

# Habilitar CORS para pruebas locales (ajusta en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos desde la carpeta `static` en /static
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    index_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    return FileResponse(index_path)


@app.get("/llm/{prompt}")
async def read_root(prompt):
    # crear una logica que me permita comunicarme con un llm
    from google import genai

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-1.5-pro", contents=prompt
    )

    return {"respuesta": response.text}

