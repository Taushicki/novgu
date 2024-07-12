from database.settings import DataBaseSettings
from fastapi import HTTPException
from pymysql import MySQLError


class DataBaseRequests:
    @staticmethod
    async def get_student_by_manid(manid: int):
        connection = None
        try:
            connection = await DataBaseSettings.setup()
            async with connection.cursor() as cursor:
                await cursor.execute(
                    "SELECT * FROM ora_students WHERE MAN_ID = %s", (manid,)
                )
                result = await cursor.fetchall()
                if not result:
                    raise HTTPException(status_code=404, detail="Student not found")
                return result
        except HTTPException as error:
            raise error
        finally:
            if connection:
                connection.close()
