# Подключаем apscheduler для создания cron-задачи
from apscheduler.schedulers.blocking import BlockingScheduler
# Импортируем значение задержки из настроек
from settings import DELAY
# Импортируем функцию самого бота
from bot import main

# Создаём крон задачу
scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', seconds=DELAY)


if __name__ == '__main__':
    print('Запускаем задачу...')
    scheduler.start()
