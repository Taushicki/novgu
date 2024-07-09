from fastapi import HTTPException
from api.services.pdf import PDF
from api.dto.student_dto import Student
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
                result = await cursor.fetchall()
                if not result:
                    raise HTTPException(status_code=404, detail="Student not found")
                return result
        finally:
            conn.close()

    @staticmethod
    async def create_pdf(student_data, output_file_name):
        await PDF().create(
            student=Student(
                courсe=student_data["COURCE"],
                group=student_data["GRP_NAME"],
                form=student_data["FS_NAME"],
                name=f"{student_data['SURNAME']} {student_data['NAME']} {student_data['PATRON']}",
                spec=f"{student_data['SPE_SHIFR']} {student_data['SPEC_NAME']}",
            ),
            output_file_name=output_file_name,
        )
