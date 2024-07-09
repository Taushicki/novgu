from fastapi import APIRouter
from typing import List
from api.services.student import UTILS as StudentUTILS


router = APIRouter()


@router.post("/getprogress/{manid}")
async def get_progress(manid: int):
    try:
        student_data = await StudentUTILS.get_student_by_manid(manid)
        if isinstance(student_data, List):
            for numb, student in enumerate(student_data):
                await StudentUTILS.create_pdf(student, f"output_{numb}.pdf")
        else:
            await StudentUTILS.create_pdf(student_data, "output.pdf")
        return {'message': 'Successfully'}
    except Exception as error:
        return {'message': error}
