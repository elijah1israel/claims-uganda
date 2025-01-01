from fastapi import FastAPI

claims = FastAPI()

@claims.get('/')
def api():
    return 'Claims Api V1'
