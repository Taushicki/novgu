from fastapi import APIRouter
from api.services.student import UTILS as StudentUTILS


router = APIRouter()


@router.post("/getprogress/{manid}")
async def get_progress(manid: int):
    return await StudentUTILS.get_student_by_manid(manid=manid)
