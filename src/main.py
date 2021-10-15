from fastapi import FastAPI

from core import define_routes

app = FastAPI(root_path='/api')

define_routes(app=app)
