from fastapi import APIRouter, Depends

from src.auth.base_config import current_user
from src.tasks.task import send_email_report_dashboard
router = APIRouter(
    prefix='/report',
    tags=["Report"]
)

@router.get('/dashbord')
def send_dashbord(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return{
        'status':'success',
        'data' : 'Письмо отправлено',
    }