from app.dal.app_dal.interface_app_dal import IAppDal


class AppDal(IAppDal):
    def read_cvs(self):
        print("read cvs")

    def create_table(self):
        print("create table")
