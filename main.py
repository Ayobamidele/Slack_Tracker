from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/track/{track}/{slack_name}")
def result(track: str, slack_name: str):
    return {
        "slack_name": f"{slack_name}",
        "current_day": "Monday",
        "utc_time": "2023-08-21T15:04:05Z",
        "track": f"{track}",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/username/repo",
        "status_code": 200,
    }
