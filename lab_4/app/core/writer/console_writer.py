from app.core.writer.i_writer import IWriter

class ConsoleWriter(IWriter):
    def write(self, data):
        print(data)
