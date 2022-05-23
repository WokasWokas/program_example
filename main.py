from parser.setting_parser import Parser
from logger.log import Logger

def main() -> None:
    logger = Logger()
    logger.update_log(
        'info',
        'Init setting parser'
    )
    setparser = Parser()
    logger.update_log(
        'info',
        'Get settings'
    )
    settings = setparser.get_settings()
    logger.save_log()

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)