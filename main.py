from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, model_validator

app = FastAPI()

class Game(BaseModel):
    id: int = Field(ge=1)
    nom: str
    editeur: str
    note: float = Field(le=10, ge=0)
    categorie: list
    sous_categorie: list

class Gaming(BaseModel):
    daGames:list[Game] = []
    @model_validator(mode="after")
    def no_doubles(self):
        all_num = []
        for game in self.daGames:
            if game.id in all_num:
                raise ValueError("Doublon d'id détecté dans la liste")
            all_num.append(game.id)
        return self
    def add_game(self, gam:Game | dict):
        if isinstance(gam, dict):
            gam = Game(**gam)
        ids = [gaming.id for gaming in self.daGames]
        if gam.id in ids:
            raise HTTPException(status_code=400, detail="Doublon d'id détecté")
        self.daGames.append(gam)
    def delete_game(self, id):
        for i in range(len(self.daGames)):
            if self.daGames[i].id == id:
                self.daGames.pop(i)
                return
        raise HTTPException(status_code=404, detail="L'id que vous avez envoyé n'as pas été trouvé")
                
games = Gaming()

games.add_game({"id": 1, "nom": "Wariodawinner", "editeur": "WarioWareInc", "note": 6.9, "categorie": ["L"], "sous_categorie": ["Action"]})
games.add_game({"id": 2, "nom": "Rosalina Galaxy", "editeur": "Luma intergalactique", "note": 5, "categorie": ["Space"], "sous_categorie": ["arf"]})
@app.get("/")
def accueil():
    return "Welcome to the underground\n How was the fall?"

@app.get("/games")
def get_games():
     return games

@app.put("/games")
def add_game(gam:Game):
    games.add_game(gam)
    return gam

@app.delete("/games/{id}")
def delete_game(id:int):
    games.delete_game(id)
    return {"message": "jeu supprimé"}