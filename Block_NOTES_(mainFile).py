import PySimpleGUI as sg
from functions import *
from datauser import *
print('::::::^^~!:..       ::::::^^~!:..       .::::::^~!:..       .:::::^^~!:..       .::::::^~!:..\n::::::^~!7^:..      ::::::^~!7^:..      .:::::^~!7^:..      .:::::^~!7^:..      .:::^^^~!7^:..      \n::::^^~!77~:..      ::::^^~!77~:..      .:::^^~!77~:..      ::::^^~!77~:..      ^?JYYYYJ?7~:..      \n::^^~~~~~^^~^:.     ::^^~~~~~^^~^:.     ::^^~~~~~^^~^:.     ::^^~~~~~^^~^:.   :?555555555J!~^:.     \n:::::::......:...   :::::::......:...   :::::::......::..   :::::::......:...^YP55555555555Y!:...   \n.   ........     ..:.   ........    ...:.   ........    ...:.   .......  .....:~Y55555555PGGG5~  ..:\n.             ..::^~.             ..::^~.             ..::^~.           ......:7P5J5555PGGGGGGG!.:^~\n..        ...::::^~!:.        ...::::^~!:.        ...::::^~!:.        ......:?GP7:.~YPGGGGGGGGGY:^~!\n:..       ::::::^^~!:..       ::::::^^~!:..       ::::::^^~!:..     ......^?GP!:..:^!PBGGGGGGGP~:^~7\n^:..      :::::^^~!7^:..      :::::^^~!7^:..      :::::^^~!7^:..  ......^JG5!...:~75BBJ7YGGGP?^:^~!7\n~^..      ::::^~!!77~^..      ::::^~~!77~^..      ::::^~!!77~^........^YG5~..:^~75BGJ!~~~7Y7^:^~~!77\n^^^:.     ::^^~~~~^^^^^:.     ::^^~~~~^^^^^:.     ::^^~~~~^^^^:.....~5GY^..:^~7P#G?~~~!!^.::^^~~~~^^\n.......   :::..............   :::..............   .::.............!5GJ^..:^~?G#P?~~~!~^.  .::.......\n       ..:.    ..         ...:.    ...        ...:.     .......:!PG?:..:^~JG#P7~~~!~^....:.     .   \n    ..::^~..           ...::^~..           ...:^^~..   ......:7PG?:..:^!JGB57~~~!~^...:^^~..        \n..:::::^~!:.        ..:::::^~!:.        ..:::::^~!:........:?GP7:..:^!YBB5!~~!!~^:.::::^~!:.        \n::::::^^~7^..       ::::::^^~7^..       ::::::^^!7:......^JGP!:..:^!YBBY!~~!!~. .:::::^^~7^..       \n:::::^^~!7^:..      :::::^^~!7^:..      :::::^^~~:.....^JG5~...:~75BBY!~~!!~.   .::::^^~!7^:..      \n:::^^~!!77~^:.      :::^^~!!7!~^:.      :::^^~^:.....^YG5~..:^~75BGJ!~~!!~:     :::^^~!!77~^:.      \n::^^^^^^^:^^^:..    ::^^^^^^^:^^^:..    ::^^^:.....~5GY^..:^~?P#G?~~~!!~^:..    ::^^^^^^^:^^^:..    \n:................   .................   .::.....:!5GJ^..:^~?G#P?~~~!~^:......   .................   \n.               ..:^.               ..::......:!PG?:..:^~JG#P7~~~!~^.       ..:^.               ..:^\n..           ..::^^~..           ..:::::....:7PG7:..:^!JGB57~~~!~:       ..::^^~..           ..::^^~\n:..       ..:::::^~!:..       ..:::::.....:?GP7:..:^!YBB5!~~~!~:      ..:::::^~!:..       ..:::::^~!\n:..       ::::::^^!7^..       :::::.....^JGP!:..:^!YBBY!~~~~~^.       ::::::^^!7^..       ::::::^~!7\n^:..      :::::^~~77^:..      ::......^JG5~...:~75BBJ!~~~~!!^:..      :::::^~~77^:..      :::::^~~!7\n~^:.      :::^^~!!!!~^:.      ......~YG5~..::~7PBGJ!~~!!!!!!~^:.      :::^^~!!!!~^:.      :::^^~!!!!\n::^::.    :^^^^^^^:::^^::.  ......~5GY^..:^~?P#G?~~~!!~^^^::::^::.    ::^^^^^^:::^^::.    ::^^^^^^::\n.......   .....................:!PGJ^..:^~?G#P?~~~!~^:.............   .................   ..........\n      ..:^.            ......:7PG?:..:^~JGBP7~~~~~^.              ..:^.               ..:^.         \n  ...::^^~..         ......:7PG7:..:^!JBB57~~~!~~~..          ...::^^~:.          ...::^^~:.        \n.::::::^~!:..      ......:?GP7:..:^!YBB5!~~~!~~^~!:..       .::::::^~!:..       .::::::^~!:..       \n::::::^~!7^..    ......^JGP!:..:^!5BBY!~~~!~^^^~!7^..       ::::::^~!7^:.       ::::::^~!7^:.       \n:::::^~!77~:.. .7~:..^YG5~...:~75BBJ!~~!!~^::^~!77~:..      .::::^~!77~:..      .::::^~!77~:..      \n:::^^~!!!!~~:.:7??7~7GY~..::~7PBGJ!~~!!^^::^~~!!!!~~:..     :::^^~!!!~~~:..     .::^^~!!!!~~:..     \n::^^^::::::::~7?777??7:.:^~?P#G?~~~!!^. ::^^^::::::::::.    ::^^^^:::::::::.    ::^^^::::::::::.    \n............:7?7777777??77G#P?~~~!~^.  ..................  ..................  ..................  .\n.          :7?777777?JY5Y557~~~!~^...:^~.              ..:^~.              ..:^~.              ..:^~\n..        .7?77777?JYYYYYYYY?!~^...::^~~:.          ..:::^~~:.          ..:::^~~:.          ..:::^^~\n:..      .7?7777?YYYYYY555Y?!::::::::^~!:..       .::::::^~!:..       .::::::^~!:..       .::::::^~!\n^:.     :?7777?YYYYYYYJ7~:    .:::::^~!7^:.       ::::::^~!7^:.       ::::::^~!7^:.       ::::::^~!7\n\~:..   ^GG5??Y55YYYJ7~:.      ::::^^~!77~:..      ::::^^~!77~:..      ::::^^~!77~:..      ::::^^~!7\n~~^:. ^GBB##GYJ?7!!~~^^:.     ::^^~~!!~~~~^:.     :::^~~!!!~~~^:.     ::^^~~!!!~~~^:.     ::^^~~!!!~\n::::.!BBBP5?!^:::::..::::..   :::::::::.:::::..   :::::::::..::::..   :::::::::..::::..   :::::::::.\n... ^Y7~:..  .......................................................................................\n    ...:^~.              ..:^~.              ..:^~.              ..:^~.              ..:^~.         \n ...:::^~~:.         ...:::^~~:.         ...:::^~~:.         ...:::^~~:.         ...:::^~~:.        ')
sg.theme('DarkBlue')
sg.popup_notify('BLOCK NOTES IS ON!', 'Please Login with your account', display_duration_in_ms = 1000 ,fade_in_duration = 500, alpha = 0.9)
#####Login#####
loginmain = True

while loginmain:
    layout = [
            [sg.Text('Welcome to Block NOTES! Block your NOTES!!!XD')],
            [sg.Text('Please login with your account below or Create a New One!')],
            [sg.Button('Create a New Account'), sg.Button('Login with an acount')],
    ]
    window = sg.Window('Welcome!', layout, icon="icone\icone.ico").Finalize()
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        exit()
    elif events == 'Create a New Account':
        window.close()
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
                if len(values['username']) < 3 and len(values['password']) < 5:
                    window['WRONG-UandP'].Update(visible=True)
                    window['WRONG-User'].Update(visible=False)
                    window['WRONG-Pass'].Update(visible=False)
                elif len(values['username']) < 3:
                    window['WRONG-User'].Update(visible=True)
                    window['WRONG-UandP'].Update(visible=False)
                    window['WRONG-Pass'].Update(visible=False)
                elif len(values['password']) < 5:
                    window['WRONG-Pass'].Update(visible=True)
                    window['WRONG-UandP'].Update(visible=False)
                    window['WRONG-User'].Update(visible=False)
                else:
                    addNEWusr(encoder(values['username']), encoder(values['password']))
                    window.close()
                    while True:
                        layout = [
                        [sg.Text('🥳🥳New User Registered.🥳🥳')],
                        [sg.Text('Now the program needs to be restarted.')],
                        [sg.OK()]
                        ]
                        window = sg.Window('Congratulations!!!', layout, icon="icone\icone.ico").Finalize()
                        events, values = window.read()
                        if events == sg.WIN_CLOSED:
                            exit()
                        if events == "OK":
                            exit()
    elif events == 'Login with an acount':
        window.close()
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
        while True:
            events, values = window.read()
            if events == sg.WINDOW_CLOSED:
                exit()
            elif events == 'Cancel':
                window.close()
                break
            elif events == 'OK':
                if encoder(values['username']) in login and login.get(encoder(values['username']))[0] == encoder(values['password']):
                    window.close()
                    loginmain = False
                    break
                else:
                    window['WRONG-UorP'].Update(visible=True)
#####Area Principal#####

WIN_W = 90
WIN_H = 25
filename = None

file_new = "Novo (CTRL+N)"
file_open = "Abrir (CTRL+O)"
file_save = "Salvar (CTRL+S)"

sg.Text()
menu_layout = (
    ["Arquivo", [file_new, file_open, file_save, "Salvar como", "---", "Sair"]],
    ["Editar", ["Tornar MAIUSCULO", "Tornar minusculo"]],
)

layout = [
    [sg.MenuBar(menu_layout)],
    [
        sg.Multiline(
            font=("Consolas", 12), text_color="white", size=(WIN_W, WIN_H), key="_BODY_"
        )
    ],
]

window = sg.Window(
    "BlockNotes",
    layout=layout,
    margins=(0, 0),
    resizable=True,
    return_keyboard_events=True,
    icon="\icone\icone.ico",
)
window.read(timeout=1)

window["_BODY_"].expand(expand_x=True, expand_y=True)


def new_file() -> str:
    window["_BODY_"].update(value="")
    filename = None
    return filename


def open_file() -> str:
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            window["_BODY_"].update(value=f.read())
    return filename


def save_file(filename: str):
    if filename not in (None, ""):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
    else:
        save_file_as()


def save_file_as() -> str:
    try:
        filename: str = sg.popup_get_file(
            "Save File",
            save_as=True,
            no_window=True,
            default_extension=".txt",
            file_types=(("Text", ".txt"),),
        )
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
    return filename


def tornar_MAIUSCULO():
    window["_BODY_"].update(value=str(values["_BODY_"]).upper())


def tornar_minusculo():
    window["_BODY_"].update(value=str(values["_BODY_"]).lower())


while True:
    event, values = window.read()

    if event in (None, "Sair"):
        window.close()
        break
    if event in (file_new, "n:78"):
        filename = new_file()
    if event in (file_open, "o:79"):
        filename = open_file()
    if event in (file_save, "s:83"):
        save_file(filename)
    if event in ("Salvar como",):
        filename = save_file_as()
    if event == "Tornar MAIUSCULO":
        tornar_MAIUSCULO()
    if event == "Tornar minusculo":
        tornar_minusculo()