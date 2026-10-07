from fastapi import APIRouter, Depends
from app.api import deps
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_user_me(current_user = Depends(deps.get_current_user)):
    return current_user
