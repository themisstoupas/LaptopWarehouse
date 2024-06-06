from fastapi import FastAPI
from controllers.productController import router as product_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


app.include_router(product_router, prefix='/product')

# uvicorn main:app --reload
# db_connection(db_config).close()
