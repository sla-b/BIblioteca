from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import _sessao_, engine, Base
from typing import List

# Cria as tabelas no banco, caso ainda não existam
Base.metadata.create_all(bind=engine)


def get_db():
    db = _sessao_()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# CRUD dos livros

@app.post('/livros/', response_model=schemas.Livro)
def registrar_livro(livro: schemas.Livro_create, db: Session = Depends(get_db)):
    novo_livro = models.Livros(**livro.model_dump()) # Ele é salvo no banco de dados em dicionário, tendo que colocar ** e utilizando o models para isso
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro


@app.get('/livros/', response_model=List[schemas.Livro])
def read_livros(db: Session = Depends(get_db)):
    return db.query(models.Livros).all() #ele somente vai retornar os livros salvos dentro do banco de dados


@app.delete('/livros/{livro_nome}', response_model=schemas.Livro)
def deletar_livro(livro_nome: str, db: Session = Depends(get_db)):
    livro = db.query(models.Livros).filter(models.Livros.nome == livro_nome).first() #É escrito o nome do livro e é procurado no banco de daods, se no "models.Livross.nome" for igual ao nome escrito, ele irá deletar

    if not livro:
        raise HTTPException(status_code=404, detail='não foi encontrado o livro')

    db.delete(livro)
    db.commit()
    return livro


@app.put('/livros/{livro_nome}', response_model=schemas.Livro)
def mudar_informacao(livro_nome: str, livro: schemas.Livro_create, db: Session = Depends(get_db)):
    livro_db = db.query(models.Livros).filter(models.Livros.nome == livro_nome).first() #Vai procurar o livro de acordo com o nome digitado

    if not livro_db:
        raise HTTPException(status_code=404, detail='não foi encontrado o livro')

    for campo, valor in livro.model_dump().items():
        setattr(livro_db, campo, valor)

    db.commit()
    db.refresh(livro_db)
    return livro_db