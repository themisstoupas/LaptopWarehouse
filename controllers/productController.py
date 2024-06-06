from fastapi import APIRouter, HTTPException
from services.productServices import ProductServices
from domain.product import Product, StockPayLoad
from typing import List, Dict

router = APIRouter()
service = ProductServices()


@router.post('/create', response_model=Product)
async def create_product(product: Product):
    created_product = service.create_product(product)
    if created_product:
        return {"message": "Product created successfully", "product": created_product}
    else:
        raise HTTPException(status_code=500, detail="Failed to create product")


@router.get('/all', response_model=List[Product])
async def get_products():
    return service.get_products()


@router.get('/specific/{name}', response_model=List[Product])
async def get_product(name: str):
    products = service.get_product_by_name(name)
    if products:
        return products
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.get('/product_statistics', response_model=Dict[str, float])
async def get_product_statistic():
    statistic = service.get_product_statistic()
    return {"statistics": statistic}


@router.delete('/delete/{name}')
async def delete_product(name: str):
    if service.delete_product(name):
        return {"message": "Product deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.put('/update/{name}', response_model=Product)
async def update_product(name: str, updated_product: Product):
    updated_product = service.update_product(name, updated_product)
    if updated_product:
        return {"message": "Product updated successfully", "product": updated_product}
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.put('/manage_stock/{name}')
async def manage_stock(name: str, payload: StockPayLoad):
    if payload.action not in ["increase", "decrease"]:
        raise HTTPException(status_code=400, detail="Invalid action. Must be 'increase' or 'decrease'")
    elif payload.quantity < 1:
        raise HTTPException(status_code=400, detail="Quantity must be a positive integer")

    products = service.get_product_by_name(name)
    if not products:
        raise HTTPException(status_code=404, detail="Product not found")

    product = products[0]
    if payload.action == "decrease" and product.quantity - payload.quantity < 0:
        raise HTTPException(status_code=400, detail="Quantity cannot be reduced to negative value")

    updated_product = service.manage_stock(name, payload.action, payload.quantity)

    if updated_product:
        return {"message": f"Stock for product '{name}' {payload.action}d by {payload.quantity}"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")
