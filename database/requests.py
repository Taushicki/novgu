from database.settings import DataBaseSettings
from fastapi import HTTPException


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

    @staticmethod
    async def get_subjects_by_manid(manid: int):
        connection = None
        try:
            connection = await DataBaseSettings.setup()
            async with connection.cursor() as cursor:
                await cursor.execute(
                    "SELECT * FROM npe_students_current_results WHERE std_id = %s",
                    (manid,),
                )
                result = await cursor.fetchall()
                if not result:
                    raise HTTPException(status_code=404, detail="Subjects not found")
                return result
        except HTTPException as error:
            raise error
        finally:
            if connection:
                connection.close()
