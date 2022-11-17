import time
import schedule
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5789952100:AAGX1CHhrORWlGLo3KUqYBYTjr0Eh3ny09k'
    bot_chatID = '5721597660'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    my_message = "Si llega este mensaje, es porque el bot funciona"
    telegram_bot_sendtext(my_message)
    print(my_message)


schedule.every().day.at("19:00").do(report)

while True:
    schedule.run_pending()
    time.sleep(1)