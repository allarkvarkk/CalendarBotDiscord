import random
import googleCalendar
import auth  # Import auth module
import serverAuth

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'test':
        return '\n'.join(googleCalendar.get_upcoming_events())

    if p_message == 'link':
       # auth.get_authorization_url()
        #auth.get_credentials()
        #serverAuth.start_server()
        return auth.get_authorization_url()

    if message == 'roll':
        return serverAuth.get_authorization_url()

    if p_message == '!help':
        return '`This is a help message you can modify.`'

    return '`I didn\'t understand what you wrote. try again`'
