from moduls import logger


def test_logger_id():
    logger_obj_1 = logger.Logger()
    logger_obj_2 = logger.Logger()
    assert id(logger_obj_1) == id(logger_obj_2)


def test_init(capsys):
    logger.Logger().init_logging()
    out, err = capsys.readouterr()
    assert err[-32:] == 'DEBUG - Logger was initialized.\n'
