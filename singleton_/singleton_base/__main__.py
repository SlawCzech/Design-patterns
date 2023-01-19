from singleton_.singleton_base.logger_base import Logger

logger = Logger('my.log')
logger.write_log('logging with singleton_ pattern')

logger2 = Logger('your.log')
assert logger is logger2
print('assertion passed')

logger2.write_log('another log record')

logger.close_log()

with open('my.log') as f:
    for line in f:
        print(line, end='')


