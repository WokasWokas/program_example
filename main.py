from parser.setting_parser import Parser
from logger.log import Logger

def init_logger() -> Logger:
    logger = Logger()
    logger.update_log('info', 'Init setting parser')
    return logger

def close_logger() -> None:
    logger.save_log()

def init_settings_parser() -> dict[str, str]:
    setparser = Parser()
    logger.update_log('info', 'Get settings')
    return setparser

def main() -> None:
    global logger
    logger = init_logger()
    
    settings_parser = init_settings_parser()
    settings = settings_parser.get_settings()

    logger.set_filename(settings['filename'])
    logger.set_log_path(settings['log_path'])
    logger.set_loglevel(settings['loglevel'])
    logger.set_timeformat(settings['timeformat'])

    # your code here

    close_logger()

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)