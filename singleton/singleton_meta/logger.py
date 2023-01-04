from datetime import datetime

from singleton.singleton_meta.singleton_meta import Singleton


class Logger(metaclass=Singleton):
    log_file = None

    def __init__(self, path):
        if type(self).log_file is None:
            type(self).log_file = open(path, 'w')

    def write_log(self, log_record):
        now = datetime.now()
        record = f'{now}: {log_record}\n'
        type(self).log_file.write(record)

    def close_log(self):
        type(self).log_file.close()
        type(self).log_file = None
