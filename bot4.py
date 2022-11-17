
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5789952100:AAGX1CHhrORWlGLo3KUqYBYTjr0Eh3ny09k'
    bot_chatID = '5721597660'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testeando")
print(test)


