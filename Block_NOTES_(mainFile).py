<<<<<<< HEAD
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
=======
#####Functions#####
def menu():
    print('|Menu|\n1 - Creat a New Block!\n2 - Find a Block\n3 - See wow many pages you have\n4 - Exit and Log Out')
    action_menu = int(input("- "))
    while action_menu < 1 and action_menu > 4:
        print('Please enter a number between 1 and 4.')
        print('|Menu|\n1 - Creat a New Block!\n2 - Find a Block\n3 - See wow many pages you have\n4 - Exit and Log Out')
        action_menu = int(input("- "))
    return(action_menu)
#####Functions END#####
#####Inícial Menú#####
print('Welcome to Block NOTES!\nBlock your NOTES!!!XD')
print('Please log in with your account below!')
#####Inícial Menú END#####
#####Log In#####
username = input('Username:\n- ')
password = input('Password:\n- ')
while username != 'SimaDinisVC' or password != 'simao78910':
    print('Wrong Username or password!')
    tasklogin = int(input('What do you want to do?\n1 - TRY AGAIN\n2 - Finish the programme\n- '))
    if tasklogin == 1:
        print('Please log in with your account below!')
        username = input('Username:\n- ')
        password = input('Password:\n- ')
    elif tasklogin == 2:
        finish = int(input('Are you sure you want to end this program?\n1 - YES\n2 - NO\n- '))
        if finish == 1:
            exit()
        elif finish == 2:
            print('Please log in with your account below!')
            username = input('Username:\n- ')
            password = input('Password:\n- ')
        else:
            print('Please enter a number between 1 and 2.')
            print('So you try again.')
            username = input('Username:\n- ')
            password = input('Password:\n- ')
    else:
        print('Please enter a number between 1 and 2.')
        print('So you try again.')
        username = input('Username:\n- ')
        password = input('Password:\n- ')
#####Log In END#####
#####Main Zone#####
#####List of Block available#####
contadorblock = 10
while True:
    action_menu = menu()
    if action_menu == 1:
        print()
    elif action_menu == 2:
        print()
    elif action_menu == 3:
        print('You have {} Blocks available.\nBy default there are 10 Blocks available in the normal plan.'.format(contadorblock))
    elif action_menu == 4:
        finish = int(input('Are you sure you want to end this program?\n1 - YES\n2 - NO\n- '))
        if finish == 1:
            print('OK,Log out READY!\nHave a nice life!')
            exit()
        elif finish == 2:
            print('OK, Glad you stayed!')
        else:
            print('Please enter a number between 1 and 2.')
>>>>>>> parent of ba0486d (Upgrade 1)
