from nonebot import get_driver

from sora.log import logger

from .scheduler import scheduler as scheduler

__version__ = "1.0.0"

DRIVER = get_driver()

PROXY = DRIVER.config.proxy

try:
    bot_admin: list[str] = [str(s) for s in DRIVER.config.bot_admin]
except Exception:
    bot_admin = []

if not bot_admin:
    logger.warning("Bot 配置", "请在配置文件中配置 Bot 管理员")
    exit()

try:
    NICKNAME: list[str] = [str(s) for s in DRIVER.config.nickname]
except Exception:
    NICKNAME: list[str] = ["林汐"]
