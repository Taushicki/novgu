from fastapi import APIRouter
from api.services.student import UTILS as StudentUTILS
from api.services.pdf import ZIP


router = APIRouter()


@router.post("/getprogress/{manid}") 
async def get_progress(manid: int):
    try:
        student_data = await StudentUTILS.get_student_by_manid(manid)
        files = []
        for numb, student in enumerate(student_data):
            StudentUTILS.create_pdf(student, f"output_{numb}.pdf")
            files.append(f"output_{numb}.pdf")
        return ZIP.create_zip(files)
    except Exception as error:
        return {"message": f'Error: {error}'}
