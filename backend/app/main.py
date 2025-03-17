from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for development (adjust later for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

models.Base.metadata.create_all(bind=database.engine)

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.Item])
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)
