import os
from django.core.wsgi import get_wsgi_application

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi import APIRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'claims.settings')

application = get_wsgi_application()


app = FastAPI()
@app.get('/')
def api():
    return 'Claims Api V1'

app.mount('/', WSGIMiddleware(application))
app.mount('/api', WSGIMiddleware(app))
