from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/dummy/')
def dummy():
    return JSONResponse(
        {"msg" : "successful setup!"}
    )