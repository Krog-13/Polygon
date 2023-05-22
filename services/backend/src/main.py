from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "hello world"


@app.get('/note')
def note():
    data = {"name": "Ricky", "comment":"I am Ricky"}
    return JSONResponse(data)


@app.post("/upload")
async def save_file(file: UploadFile):
    """
    Translator
    :return: file
    """
    files = file.file.read()
    return files


@app.get("/download/")
async def download(file_id: str):
    """
    receive file from remote api
    """
    return {"file_id": file_id}
