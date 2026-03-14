from app.dal.application_dal.interface_application_dal import IApplicationDal


class ApplicationDal(IApplicationDal):
    def read_cvs(self):
        print("read cvs")

    def create_table(self):
        print("create table")
