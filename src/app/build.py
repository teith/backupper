from fastapi import FastAPI, Depends
from app.deps import get_archiver, get_provider
from archive_builder.archiver import Archiver
from cloud.provider import Provider

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/archive")
async def archive(archiver: Archiver = Depends(get_archiver),
                  provider: Provider = Depends(get_provider)):
    zip_dir = archiver.create_archive()
    # provider.upload(archive_path)
    return {"message": zip_dir}
