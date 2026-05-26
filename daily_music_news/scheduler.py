"""APScheduler setup and job management."""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from config import Config

logger = logging.getLogger(__name__)


class NewsScheduler:
    """Manages scheduled tasks for news delivery."""

    def __init__(self):
        """Initialize the scheduler."""
        self.scheduler = BackgroundScheduler()
        self.job_id = "daily_music_news"

    def schedule_daily_news(self, job_func, hour: int = 8, minute: int = 0):
        """Schedule a daily job at specific time.

        Args:
            job_func: Function to execute
            hour: Hour in 24-hour format
            minute: Minute
        """
        try:
            # Parse schedule time from config
            schedule_time = Config.SCHEDULE_TIME
            if isinstance(schedule_time, str):
                parts = schedule_time.split(":")
                hour = int(parts[0])
                minute = int(parts[1]) if len(parts) > 1 else 0

            logger.info(f"Scheduling daily job at {hour:02d}:{minute:02d}")

            self.scheduler.add_job(
                job_func,
                CronTrigger(hour=hour, minute=minute),
                id=self.job_id,
                name="Daily Music News Delivery",
                replace_existing=True,
            )

            logger.info(
                f"✅ Job scheduled successfully. Next run: {self.scheduler.get_job(self.job_id).next_run_time}"
            )

        except Exception as e:
            logger.error(f"Failed to schedule job: {e}")
            raise

    def start(self):
        """Start the scheduler."""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("✅ Scheduler started")
        else:
            logger.info("Scheduler is already running")

    def stop(self):
        """Stop the scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("Scheduler stopped")

    def get_next_run(self):
        """Get the next scheduled run time."""
        job = self.scheduler.get_job(self.job_id)
        if job:
            return job.next_run_time
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    def test_job():
        logger.info("Test job executed!")

    scheduler = NewsScheduler()
    scheduler.schedule_daily_news(test_job, hour=8, minute=0)
    scheduler.start()

    print(f"Next run: {scheduler.get_next_run()}")
    print("Scheduler running. Press Ctrl+C to stop.")

    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        scheduler.stop()
