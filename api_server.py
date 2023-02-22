import main
import os
import shutil
import uvicorn

from fastapi import FastAPI, File, UploadFile, Response, status, Depends
from starlette.requests import Request


def make_classification(file_name: str):
    file_name = os.path.join("input_images", file_name)
    score, classified_class = main.classification(file_name, model, class_names)
    return score, classified_class

if __name__ == "__main__":
    uvicorn.run("api_server:app", port=8000, log_level="info")
else:
    app = FastAPI()
    model, class_names = main.run_model()

    @app.post("/classifier_image", status_code=201)
    async def receive_input(
    request: Request,
    response: Response,
    file:UploadFile = File(...)
    ):

        _, name = os.path.split(file.filename)
        path = "input_images/"
        if not os.path.isdir(path):
            os.mkdir(path=path)
        
        path_file = path + name
        with open(path_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        score, classified_class = make_classification(file_name=file.filename)

        response.status_code = status.HTTP_201_CREATED
        return {
            "This image is a": classified_class,
            "With": f"{score} percent confidence"
        }
