from fastapi import APIRouter, HTTPException
from database.models import Student

router = APIRouter()


@router.post("/getprogress/{manid}")
async def get_progress(manid: int):
    students = await Student.filter(MAN_ID=manid)
    if not students:
        raise HTTPException(status_code=404, detail="Student not found")

    for student in students:
        student_data = {
            "COURCE": student.COURCE,
            "GRP_NAME": student.GRP_NAME,
            "FS_NAME": student.FS_NAME,
            "NAME": student.NAME,
            "SURNAME": student.SURNAME,
            "PATRON": student.PATRON,
            "SPE_SHIFR": student.SPE_SHIFR,
            "SPEC_NAME": student.SPEC_NAME,
            "BIRTHDAY": student.BIRTHDAY,
            "PHONE": student.PHONE,
            "EMAIL": student.EMAIL,
        }

    print(student_data)
