from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Veiaco(Base):
    __tablename__ = 'veiaco'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    valor = Column(Float)

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor