from loguru import logger

from core.twitter import Bot

logger.add('rinzler.log', rotation='144 MB')
rinzler = Bot()

msg, is_successful = rinzler.tweet_word()
if is_successful:
    logger.success(msg)
else:
    logger.error(msg)
