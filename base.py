import uvicorn

if __name__ == '__main__':
    uvicorn.run("services.backend.src.main:app", host="127.0.0.1", port=5000, reload=True)