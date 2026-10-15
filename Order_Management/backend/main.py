from fastapi import FastAPI

app = FastAPI(title="My OrderManagement Application", description="Order Management application.", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Order Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
