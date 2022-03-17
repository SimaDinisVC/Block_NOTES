from PySimpleGUI import PySimpleGUI as sg
sg.theme('DarkBlue')
sg.popup_notify('BLOCK NOTES IS ON!', 'Please Login with your account', display_duration_in_ms = 3000 ,fade_in_duration = 1000, alpha = 0.9)
def LogLayout(value):
    if value == 0:
        layout = [
            [sg.Text('Welcome to Block NOTES! Block your NOTES!!!XD')],
            [sg.Text('Please login with your account below or Create a New One!')],
            [sg.Button('Create a New Account'), sg.Button('Login with an acount')],
            
        ]
        window = sg.Window('Welcome!', layout, icon="icone\icone.ico").Finalize()

    elif value == 1:
        layout = [
        [sg.Text('Username'), sg.Input(key='username')],
        [sg.Text('Password'), sg.Input(key='password', password_char='⚫')],
        [
            sg.Text('Your Username needs to be 3 or more characters.', key = 'WRONG-User', visible=False),
            sg.Text('Your Username needs to be 3 or more characters and the Password needs to be 5 or more characters.', key = 'WRONG-UandP', visible=False),
            sg.Text('Your Password needs to be 5 or more characters.', key = 'WRONG-Pass', visible=False),
            sg.Text('Username or Password are wrong. Try again.', key = 'WRONG-UorP', visible=False)
        ],
        [sg.OK(), sg.Cancel()]
        ]
        window = sg.Window("Put your Credential's", layout, icon="icone\icone.ico").Finalize()

    elif value == 2:
        layout = [
        [sg.Text('🥳🥳New User Registered.🥳🥳')],
        [sg.Text('Now the program needs to be restarted.')],
        [sg.OK()]
        ]
        window = sg.Window('Congratulations!!!', layout, icon="icone\icone.ico").Finalize()

    return window