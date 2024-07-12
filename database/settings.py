import os
from dotenv import load_dotenv
from fastapi import HTTPException
from pymysql import MySQLError
import aiomysql

load_dotenv()


class DataBaseSettings:
    @staticmethod
    async def setup():
        try:
            return await aiomysql.connect(
                host=os.getenv("DB_HOST"),  # type: ignore
                port=int(os.getenv("DB_PORT")),  # type: ignore
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),  # type: ignore
                db=os.getenv("DB_NAME"),
                cursorclass=aiomysql.DictCursor,
            )
        except MySQLError as error:
            raise HTTPException(
                status_code=500, detail=f"Database connection failed: {str(error)}"
            )
