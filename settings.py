from os import environ

# Настройки записи, можно не менять, но на всякий случай
OWNER_ID = -174105461
POST_ID = 6713149

# Токен(ы) пользователей
TOKENS = environ.get('TOKENS').split(',')

# Задержка в секундах (на данный момент 4 часа и 15 секунд)
DELAY = (60 * 60 * 4) + 15

# Удалять коментарий? (True - да, False - нет)
DELETE_COMMENTS = False
