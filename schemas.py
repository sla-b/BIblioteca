from pydantic import BaseModel


class LivroBase(BaseModel):
    nome: str
    autor: str
    ano: int


class Livro_create(LivroBase):
    """Dados recebidos para criar/atualizar um livro."""
    pass


class Livro(LivroBase):
    """Dados retornados pela API (inclui o id gerado pelo banco)."""
    id: int

    class Config:
        from_attributes = True