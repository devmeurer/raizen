from typing import Optional

from fastapi import Depends, FastAPI, File, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.config import create_tables, get_db
from app.database.models import Product
from app.services.csv_download import generate_csv
from app.services.csv_process import process_csv

app = FastAPI()


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


@app.post("/products/upload")
def create_product(file: bytes = File(...), db: Session = Depends(get_db)):
    try:
        products = process_csv(file)
        for product in products:
            db.add(product)
        db.commit()
        db.close()
        return {"message": "Dados inseridos com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao processar arquivo")


@app.get("/products/download")
def download_products(
    name: Optional[str] = None,
    description: Optional[str] = None,
    price: Optional[float] = None,
    quantity: Optional[int] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Product)
    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
        return generate_csv(query)
    if description:
        query = query.filter(Product.description.ilike(f"%{description}%"))
        return generate_csv(query)
    if price:
        query = query.filter(Product.price == price)
        return generate_csv(query)
    if quantity:
        query = query.filter(Product.quantity == quantity)
        return generate_csv(query)
    return generate_csv(query.all())


@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        new_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        db.close()
        return {"id": new_product.id, "message": "Produto inserido com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao inserir produto")


@app.get("/products/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            return product
        else:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao ler produto")


@app.put("/products/{product_id}")
def update_product(
    product_id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    try:
        product_update = db.query(Product).filter(Product.id == product_id).first()
        if product_update:
            product_update.name = product.name
            product_update.description = product.description
            product_update.price = product.price
            product_update.quantity = product.quantity
            db.commit()
            db.refresh(product_update)
            db.close()
            return {
                "id": product_update.id,
                "message": "Produto atualizado com sucesso",
            }
        else:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar produto,{e}")


@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if product:
        db.delete(product)
        db.commit()
        db.close()
        return {"message": "Produto excluído com sucesso"}
    else:
        db.close()
        return {"message": "Produto não encontrado"}
