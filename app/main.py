# SPDX-FileCopyrightText: 2026 Sarah Gäumann <sarahgaeumann01@gmail.com>
#
# SPDX-License-Identifier: MIT

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Running."}
