from database.requests import DataBaseRequests
from api.services.pdf import PDF
from api.dto.student_dto import Student
from fastapi import HTTPException


class UTILS:
    @staticmethod
    async def get_student_by_manid(manid: int):
        try:
            return await DataBaseRequests.get_student_by_manid(manid=manid)
        except Exception as error:
            raise error

    @staticmethod
    def create_pdf(student_data, output_file_name):
        PDF().create(
            student=Student(
                course=student_data["COURCE"],
                group=student_data["GRP_NAME"],
                form=student_data["FS_NAME"],
                name=f"{student_data['SURNAME']} {student_data['NAME']} {student_data['PATRON']}",
                spec=f"{student_data['SPE_SHIFR']} {student_data['SPEC_NAME']}",
            ),
            output_file_name=output_file_name,
        )
