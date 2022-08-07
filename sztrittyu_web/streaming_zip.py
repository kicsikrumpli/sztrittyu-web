import asyncio
import json
from io import BytesIO
from typing import List, Tuple
from zipfile import ZipFile

import aiohttp


async def get_content(url) -> bytes:
    async with aiohttp.ClientSession() as session, \
            session.get(url) as response:
        return await response.json()


async def make_zip(name_url_pairs: List[Tuple[str, str]]):
    async def write_zip(byte_buffer_: BytesIO):
        with ZipFile(byte_buffer_, 'w') as zip_file:
            for name, url in name_url_pairs:
                content = await get_content(url)
                content_bytes = json.dumps(content, indent=2).encode('utf-8')
                zip_file.writestr(f'{name}.txt', content_bytes)
        byte_buffer_.seek(0)
        return byte_buffer_

    byte_buffer = await write_zip(BytesIO())

    for chunk in byte_buffer:
        yield chunk

    byte_buffer.close()


async def main():
    with open('my_zip.zip', 'wb') as out_file:
        async for chunk in make_zip([('file 1', "https://baconipsum.com/api/?type=meat-and-filler"),
                                     ('file 2', "https://baconipsum.com/api/?type=all-meat&paras=2&start-with-lorem=1"),
                                     ('file 3', "https://baconipsum.com/api/?type=all-meat&sentences=1&start-with-lorem=1")]):
            out_file.write(chunk)
            # yield chunk


if __name__ == '__main__':
    asyncio.run(main())
