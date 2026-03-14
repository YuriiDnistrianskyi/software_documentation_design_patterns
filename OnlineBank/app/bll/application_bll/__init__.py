from app.bll.application_bll.application_bll import ApplicationBll
from app.dal.application_dal import app_dal

app_bll = ApplicationBll(app_dal)
