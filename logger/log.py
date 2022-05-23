from time import time, gmtime, strftime
import logger.errors as error

def get_log_level() -> int:
    _available_levels = [0, 1]

    loglevel: int
    with open('logger/loglevel', mode='r') as file:
        loglevel = int(file.read(1))
        file.close()
    
    if not loglevel in _available_levels:
        raise error.UnknowLoggerLevel(f'Unknow log level {loglevel}')
    return loglevel

def save_file(path: str, filename: str, data: str) -> None:
    with open(file=f'{path}\\{filename}', mode='w') as file:
        file.write(data)
        file.close()

class Logger:
    def __init__(self) -> None:
        self.loglevel = get_log_level()
        self.timeformat = '%H %M %S'
        self.log_path = 'logs'
        self.data = ""
        self.update_log('info', 'Logger started!')
        
    def update_log(self, type: str, message: str) -> None:
        if self.loglevel == 0: return
        timestamp = strftime(self.timeformat, gmtime(time()))
        self.data += f'{timestamp} [{type}] : {message}\n'
    
    def save_log(self) -> None:
        if self.loglevel == 0: return
        self.update_log('info', 'Logger closing!')
        timestamp = strftime(self.timeformat, gmtime(time()))
        save_file(self.log_path, f'{timestamp}.log', data=self.data)