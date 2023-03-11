from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Juan"

@app.get("/url")
async def url():
    return { "url_curso":"https://https://www.youtube.com" } 

# comando para iniciar el servidor de fastApi en la  terminal "python -m uvicorn main:app --reload"

