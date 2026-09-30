from database import Base
from sqlalchemy import Column, Integer, String

class Livros(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    autor = Column(String(100))
    ano = Column(Integer)
    editora = Column(String(50))
