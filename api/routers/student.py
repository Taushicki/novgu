from fastapi import APIRouter
from api.services.student import UTILS as StudentUTILS
from api.services.pdf import ZIP


router = APIRouter()


@router.post("/getprogress/{manid}")
async def get_progress(manid: int):
    try:
        files = []
        student_data = await StudentUTILS.get_student_by_manid(manid)
        for numb, student in enumerate(student_data):
            student_subjects = await StudentUTILS.get_subjects_by_manid(int(student["STD_ID"]))
            StudentUTILS.create_pdf(student, student_subjects, f"{student['MAN_ID']}_{student['STD_ID']}.pdf")
            files.append(f"{student['MAN_ID']}_{student['STD_ID']}.pdf")
        return ZIP.create_zip(files)
    except Exception as error:
        return {"message": f"Error: {error}"}
