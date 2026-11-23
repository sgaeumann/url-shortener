# SPDX-FileCopyrightText: 2026 Sarah Gäumann <sarahgaeumann01@gmail.com>
#
# SPDX-License-Identifier: MIT

from fastapi import FastAPI
from loguru import logger

from .url_cleaning import clean_url
from .url_hash import hash_url

app = FastAPI()


@app.get("/")
async def root():
    logger.info("app running.")
    return {"message": "Running."}


@app.post("/url")
async def generate_url(url: str):
    logger.info("generating url...")
    # cleanse url
    url = clean_url()
    # compute hash
    url = hash_url(url)
    # return shortened url
    return {"result": url}
