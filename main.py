from fastapi import FastAPI
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()


@app.get("/llm/{prompt}")
async def read_root(prompt):
    #crear una logica que me permita comunicarme con un llm
    from google import genai

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-1.5-pro", contents = prompt
    )
    print(response.text)


    return {"respuesta": response.text}

