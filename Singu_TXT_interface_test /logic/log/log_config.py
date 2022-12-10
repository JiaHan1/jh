import logging.handlers
import logging


def init_log_config(name, filename, when='midnight', interval=1, backup_count=1):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    st = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when=when,
                                                   interval=interval,
                                                   backupCount=backup_count,
                                                   encoding='utf-8')
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    st.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(st)
    logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    a1 = init_log_config('a1', 'a1.log')
    a1.warning('qqqqq')

    a2 = init_log_config('a2', 'a2.log')
    a2.warning('nnnnn')
