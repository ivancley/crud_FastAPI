from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from models import Base, Veiaco

app = FastAPI()


DATABASE_URL = "sqlite:///db.sqlite3"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

class VeiacoCreate(BaseModel):
    nome: str
    valor: float

class VeiacoResponse(BaseModel):
    id: int
    nome: str
    valor: float

class VeiacoUpdate(BaseModel):
    nome: str
    valor: float

@app.get("/itens/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/veiacos", response_model=list[VeiacoResponse])
def get_veiacos():
    db = SessionLocal()
    veiacos = db.query(Veiaco).all()
    db.close()
    return veiacos


@app.post("/veiacos/novo", response_model=VeiacoResponse)
def create_veiaco(veiaco_data: VeiacoCreate):
    db = SessionLocal()
    veiaco = Veiaco(nome=veiaco_data.nome, valor=veiaco_data.valor)
    db.add(veiaco)
    db.commit()
    db.refresh(veiaco)
    db.close()
    return veiaco

@app.get("/veiacos/{veiaco_id}", response_model=VeiacoResponse)
def get_veiaco(veiaco_id: int):
    db = SessionLocal()
    veiaco = db.query(Veiaco).filter(Veiaco.id == veiaco_id).first()
    db.close()
    if not veiaco:
        raise HTTPException(status_code=404, detail="Veiaco não encontrado")
    return veiaco

@app.put("/veiacos/{veiaco_id}", response_model=VeiacoResponse)
def update_veiaco(veiaco_id: int, veiaco_data: VeiacoUpdate):
    db = SessionLocal()
    veiaco = db.query(Veiaco).filter(Veiaco.id == veiaco_id).first()
    if not veiaco:
        raise HTTPException(status_code=404, detail="Veiaco nnão encontrado")
    veiaco.nome = veiaco_data.nome
    veiaco.valor = veiaco_data.valor
    db.commit()
    db.refresh(veiaco)
    db.close()
    return veiaco

@app.delete("/veiacos/{veiaco_id}")
def delete_veiaco(veiaco_id: int):
    db = SessionLocal()
    veiaco = db.query(Veiaco).filter(Veiaco.id == veiaco_id).first()
    if not veiaco:
        raise HTTPException(status_code=404, detail="Veiaco não encontrado")
    db.delete(veiaco)
    db.commit()
    db.close()
    return {"message": "Veiaco deletado!!!"}