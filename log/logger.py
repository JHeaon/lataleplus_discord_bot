import logging
import os
from notify.discord_notifier import DiscordNotifier


class ErrorHandler(logging.Handler):
    def emit(self, record):
        if record.levelname == 'ERROR':
            DiscordNotifier(os.environ.get("DISCORD_ERROR_API")).send_message(f"{record.message} 에러가 발생하였습니다.")


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

error_handler = ErrorHandler()
file_handler = logging.FileHandler('./log/log.log', mode='w')

logging.getLogger().setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logging.getLogger().addHandler(error_handler)
logging.getLogger().addHandler(file_handler)
