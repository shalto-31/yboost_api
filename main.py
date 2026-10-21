from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def accueil():
    return "Welcome to the underground\n How was the fall?"