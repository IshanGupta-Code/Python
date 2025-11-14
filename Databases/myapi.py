# CRUD / HTTP
# Create - POST
# Read - GET
# Update - PUT
# Delete - DELETE

from fastapi import FastAPI, HTTPException, Path, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# EndPoint -> It is like URL
# www.ishangupta.com/  -> "/" this is an endpoint of an URL

@app.get("/")
def root():
    return{"message":"Welcome to my first api",
           "2message": "Hello"}
