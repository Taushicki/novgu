from pydantic import BaseModel


class UserDTO(BaseModel):
    COURCE: int
    GRP_NAME: str
    FS_NAME: str
    NAME: str
    SURNAME: str
    PATRON: str
    SPE_SHIFR: str
    SPEC_NAME: str
