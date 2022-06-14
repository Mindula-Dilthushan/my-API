from fastapi import FastAPI

app = FastAPI()

mindula = [
    {
        "name": "Mindula",
        "age": 23
    },
    {
        "name": "Dilthushan",
        "age":23
    }]


@app.get("/")
async def root():
    return {"message": "Hello my-API"}


@app.get("/mindula")
def get_mindula():
    return mindula
