import os
import log.logger

from apscheduler.schedulers.background import BackgroundScheduler
from crawl.crawler import Crawler
from handle.handler import Handler
from notify.discord_notifier import DiscordNotifier
from observer.monitor import Monitor

if __name__ == "__main__":

    def schedule_time(hour, minute):
        return {'hours': hour, "minutes": minute}


    monitor_list = [
        Monitor(Crawler(os.environ.get("ANNOUNCEMENT_API")),
                Handler(os.environ.get("DB"), "Announcement"),
                DiscordNotifier(os.environ.get("DISCORD_ANNOUNCEMENT_API"))),

        Monitor(Crawler(os.environ.get("INSPECTION_UPDATE_API")),
                Handler(os.environ.get("DB"), "InspectionUpdate"),
                DiscordNotifier(os.environ.get("DISCORD_INSPECTION_UPDATE_API"))),

        Monitor(Crawler(os.environ.get("DEVELOPER_NOTE_API")),
                Handler(os.environ.get("DB"), "DeveloperNote"),
                DiscordNotifier(os.environ.get("DISCORD_DEVELOPER_NOTE_API"))),

        Monitor(Crawler(os.environ.get("EVENT_API")),
                Handler(os.environ.get("DB"), "Event"),
                DiscordNotifier(os.environ.get("DISCORD_EVENT_API"))),

        Monitor(Crawler(os.environ.get("EVENT_WINNER_API")),
                Handler(os.environ.get("DB"), "EventWinner"),
                DiscordNotifier(os.environ.get("DISCORD_EVENT_WINNER_API"))),

        Monitor(Crawler(os.environ.get("FREE_BULLET_IN_BOARD")),
                Handler(os.environ.get("DB"), "FreeBulletinBoard"),
                DiscordNotifier(os.environ.get("DISCORD_FREE_BULLET_IN_BOARD_API"))),

    ]

    scheduler = BackgroundScheduler(timezone='Asia/Seoul')

    for monitor in monitor_list:
        scheduler.add_job(monitor.run, "interval", seconds=10)

    scheduler.start()

    while True:
        pass
