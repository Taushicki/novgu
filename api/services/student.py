from fastapi import HTTPException
from database.settings import DataBaseSettings


class UTILS:
    @staticmethod
    async def get_student_by_manid(manid: int):
        conn = await DataBaseSettings.setup()
        try:
            async with conn.cursor() as cursor:
                await cursor.execute(
                    "SELECT * FROM ora_students WHERE MAN_ID = %s", (manid,)
                )
                result = await cursor.fetchone()
                if not result:
                    raise HTTPException(status_code=404, detail="Student not found")
                return result
        finally:
            conn.close()
