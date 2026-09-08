from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Placar API")

class JogadorEntrada(BaseModel):
    nome: str = Field(min_length=5, max_length=50)

class Jogador(BaseModel):
    id: int
    nome: str = Field(min_length=5, max_length=50)

jogadores: list[Jogador] = []

@app.post("/jogador")
def criar_jogador(dados: JogadorEntrada):
    novo = Jogador(id=len(jogadores) + 1, **dados.model_dump())
    jogadores.append(novo)
    return novo

@app.get("/jogador/{id}")
def pegar_jogador(id: int):
    for jogador in jogadores:
        if jogador.id == id:
            return jogador
    raise HTTPException(status_code=404, detail="jogador nao encontrado")

@app.delete("/jogador/{id}")
def apagar_jogador(id: int):
    for jogador in jogadores:
        if jogador.id == id:
            jogadores.remove(jogador)
            return {"status": True}
    raise HTTPException(status_code=404, detail="jogador nao encontrado")

@app.put("/jogador/{id}", response_model=Jogador)
def atualizar_jogador(id: int, dados: JogadorEntrada):
    for i,jogador in enumerate(jogadores):
        if jogador.id == id:
            atualizado = Jogador(id=len(jogadores) + 1, **dados.model_dump())
            jogadores[i] = atualizado
            return atualizado
    raise HTTPException(status_code=404, detail="jogador nao encontrado")

@app.get("/jogadores", response_model=list[Jogador])
def pegar_jogadores():
    return jogadores