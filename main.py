import datetime
from fastapi import FastAPI, Response, Query

app = FastAPI()


def get_time_and_day():
    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()

    # Get the day of the week
    day_of_week = utc_now.strftime("%A")

    # Format the time
    utc_time = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Return as a dictionary
    return {"Day of Week": day_of_week, "UTC Time": utc_time}


@app.get("/api")
async def get_data(
    response: Response,
    slack_name: str = Query(..., description="The name of the slack user"),
    track: str = Query(..., description="The track of the user"),
):
    # Get the result for time and day
    time_and_day_result = get_time_and_day()

    # Get the current status code
    current_status_code = response.status_code

    # Return as a dictionary
    return {
        "slack_name": f"{slack_name}",
        "current_day": time_and_day_result["Day of Week"],
        "utc_time": time_and_day_result["UTC Time"],
        "track": f"{track}",
        "github_file_url": "https://github.com/Ayobamidele/Slack_Tracker/blob/main/main.py",
        "github_repo_url": "https://github.com/Ayobamidele/Slack_Tracker",
        "status_code": current_status_code or 200,
    }
