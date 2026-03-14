from app.bll.application_bll.interface_application_bll import IApplicationBll
from app.dal.application_dal.interface_application_dal import IApplicationDal


class ApplicationBll(IApplicationBll):
    def __init(self, dal: IApplicationDal):
        self.__dal: IApplicationDal = dal

    def read_csv(self):
        pass

    def create_table(self):
        pass
