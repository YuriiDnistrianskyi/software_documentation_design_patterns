from app.dal.i_app_dal import IAppDal

class AppDal(IAppDal):
    def read_data_source(self):
        print('read')

    def write_data(self):
        print('write')
