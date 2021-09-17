from telegram_bot import Telegram
from Config import Configs

if __name__ == '__main__':
    configs = Configs()
    telegram = Telegram(configs.TOKEN)

    getMe = telegram.getMe()
    updates = telegram.getUpdates()

    message = telegram.sendMessage(-521135858, 'Test')

    # print(getMe)
    print(updates)
    print(message)
