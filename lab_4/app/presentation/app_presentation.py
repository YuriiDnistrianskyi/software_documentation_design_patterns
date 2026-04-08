from app.bll.i_app_bll import IAppBll

class AppPresentation:
    def __init__(self, bll: IAppBll):
        self.bll = bll