from typing import List

from fastapi import FastAPI
from starlette.responses import StreamingResponse

from sztrittyu_web.screenshot import Req
from sztrittyu_web.streaming_zip import make_zip

app = FastAPI()

dummy_content = b"""my dummy content"""


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/zip")
async def get_dummy_zip():
    return StreamingResponse(
        content=make_zip([('file 1', "https://baconipsum.com/api/?type=meat-and-filler"),
                          ('file 2', "https://baconipsum.com/api/?type=all-meat&paras=2&start-with-lorem=1"),
                          ('file 3', "https://baconipsum.com/api/?type=all-meat&sentences=1&start-with-lorem=1")]),
        media_type="application/zip"
    )


# @app.post("/zip")
async def get_zip(items: List[Req]):
    return StreamingResponse(
        content=make_zip([(item.name, item.url) for item in items]),
        media_type="application/zip"
    )
