from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db, book = request.parameter)
    return Response(code=200, status='Ok', message='libro creato con successo').dict(exclude_none=True)

@router.get('/')
async def get(db:Session=Depends(get_db)):
    book = crud.get_book(db,0,100)
    return Response(code=200, status='Ok', message='dati ritirati con successo', result=book).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id:int, db:Session=Depends(get_db)):
    book = crud.get_book_by_id(db, id)
    return Response(code=200, status='Ok', message='libro ritirato con successo', result=book).dict(exclude_none=True)

@router.put('/update')
async def update_book(request: RequestBook, db:Session=Depends(get_db)):
    book = crud.update_book(db, book_id=request.parameter.id, title=request.parameter.title, description=request.parameter.description)
    return Response(code=200, status='Ok', message='libro aggiornato', result=book)

@router.delete('/{id}')
async def delete_book(id:int, db:Session=Depends(get_db)):
    book = crud.delete_book(db, book_id = id)
    return Response(code=200, status='Ok', message='libro cancellato').dict(exclude_none=True)
