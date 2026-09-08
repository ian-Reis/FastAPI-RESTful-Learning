from typing_extensions import Annotated
from fastapi import FastAPI, Query

app = FastAPI(title="Placar API")

@app.get("/saude")
def saude():
    return {"status": "ok"}

@app.get("/jogos/{slug}")
def detalhe_do_jogo(slug: str):
    return {"slug": slug}

@app.get("/placar")
def placar(jogo: str, limite: Annotated[int, Query(ge=1, le=100)] = 10):
    return {"jogo": jogo, "limite": limite}

@app.get("/eco/{texto}")
def eco(texto: str):
    return {"texto_invertido": texto[::-1]}