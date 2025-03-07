import logging
import logging.config
import time


logging.config.fileConfig(fname='conf/rotation_logger.conf')
logger = logging.getLogger(__name__)


for _ in range(1000):
    logger.debug('デバッグログ')
    logger.info('インフォログ')
    logger.warning('ワーニングログ')
    logger.error('エラーログ')
    logger.critical('クリティカルログ')
    time.sleep(1)
