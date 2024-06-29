import os
from dotenv import load_dotenv
import aiomysql

load_dotenv()


class DataBaseSettings:
    @staticmethod
    async def setup():
        return await aiomysql.connect(
            host=os.getenv("DB_HOST"),  # type: ignore
            port=int(os.getenv("DB_PORT")),  # type: ignore
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),  # type: ignore
            db=os.getenv("DB_NAME"),
            cursorclass=aiomysql.DictCursor,
        )
