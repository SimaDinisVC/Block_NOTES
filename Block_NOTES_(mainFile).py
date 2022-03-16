from functions import *
from datauser import *
from GUI import *
#####Login#####
loginmain = True
while True:
    window = LogLayout(0)
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        exit()
    elif events == 'Create a New Account':
        window.close()
        window = LogLayout(1)
        while True:
            events, values = window.read()
            if events == sg.WIN_CLOSED:
                exit()
            elif events == 'Cancel':
                window['WRONG-UandP'].Update(visible=False)
                window['WRONG-User'].Update(visible=False)
                window['WRONG-Pass'].Update(visible=False)
                window.close()
                break
            elif events == 'OK':
                if len(values['username']) < 3 and len(values['password']) < 8:
                    window['WRONG-UandP'].Update(visible=True)
                    window['WRONG-User'].Update(visible=False)
                    window['WRONG-Pass'].Update(visible=False)
                elif len(values['username']) < 3:
                    window['WRONG-User'].Update(visible=True)
                    window['WRONG-UandP'].Update(visible=False)
                    window['WRONG-Pass'].Update(visible=False)
                elif len(values['password']) < 8:
                    window['WRONG-Pass'].Update(visible=True)
                    window['WRONG-UandP'].Update(visible=False)
                    window['WRONG-User'].Update(visible=False)
                else:
                    addNEWusr(encoder(values['username']), encoder(values['password']))
                    window.close()
                    while True:
                        window = LogLayout(2)
                        events, values = window.read()
                        if events == sg.WIN_CLOSED:
                            exit()
                        if events == "OK":
                            exit()
    elif events == 'Login with an acount':
        window.close()
        window = LogLayout(1)
        while True:
            events, values = window.read()
            if events == sg.WINDOW_CLOSED:
                exit()
            elif events == 'Cancel':
                window.close()
                break
            elif events == 'OK':
                if encoder(values['username']) in login and login.get(encoder(values['username']))[0] == encoder(values['password']):
                    print('Entrou!!!')
                    loginmain = False
                else:
                    window['WRONG-UorP'].Update(visible=True)
#####Login END#####
#####Main Zone#####
