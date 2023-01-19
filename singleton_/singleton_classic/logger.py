from datetime import datetime


class Logger:
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in dir(Logger):
            Logger._instance = Logger()
        return Logger._instance

    def open_log(self, path):
        type(self).log_file = open(path, 'w')

    def write_log(self, log_record):
        now = datetime.now()
        record = f'{now}: {log_record}\n'
        type(self).log_file.write(record)

    def close_log(self):
        type(self).log_file.close()
        type(self).log_file = None


l1 = Logger.instance()
l1.open_log('my.log')
l1.write_log('1234')
l1.close_log()

with open('my.log') as f:
    for line in f:
        print(line)
