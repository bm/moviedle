from fastapi import FastAPI

import pandas as pd
import json

app = FastAPI()

df = pd.read_csv("rotten_tomatoes_movies.csv")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/titles")
# need list of titles for auto-complete feature
async def get_titles():
    adj = df.fillna("")
    return adj["title"].to_list()

@app.get("/movies")
async def get_movies():
    return parse_csv(df)

def parse_csv(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed
