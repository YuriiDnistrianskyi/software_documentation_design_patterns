from app.core.writer.i_writer import IWriter

class TXTWriter(IWriter):
    def write(self, data):
        with open('data.txt', 'w', encoding='utf-8') as file:
            file.write(data)
