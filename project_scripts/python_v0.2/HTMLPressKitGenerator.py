import time

import keyboard

import LitteHelp
import ScreensAndFunctions


# python -m nuitka --onefile --windows-onefile-tempdir-spec=%TEMP%\\onefile_%PID%_%TIME% HTMLPressKitGenerator.py


LANGUAGE = 1
GO_BACK = False
ACTIVE_SCREEN = 0
LitteHelp.CheckRepo('./images')


def Voltar(event):
    global GO_BACK
    if event.name == 'esc':
        GO_BACK = True


while True:
    # ESCOLHA O IDIOMA
    if ACTIVE_SCREEN == 0:
        LitteHelp.LimparTela()
        ScreensAndFunctions.ChooseTheLanguage()

        while True:
            if keyboard.read_key() == '1':
                ACTIVE_SCREEN = 1
                LANGUAGE = 1
                break
            elif keyboard.read_key() == '2':
                ACTIVE_SCREEN = 1
                LANGUAGE = 2
                break
        time.sleep(0.15)

    # MENU
    if ACTIVE_SCREEN == 1:
        LitteHelp.LimparTela()
        ScreensAndFunctions.MainMenu(LANGUAGE)

        while True:
            if keyboard.read_key() == '1':
                ACTIVE_SCREEN = 2
                break
            elif keyboard.read_key() == '2':
                ACTIVE_SCREEN = 3
                break
            elif keyboard.read_key() == 'esc':
                ACTIVE_SCREEN = 4
                break
        time.sleep(0.15)

    elif ACTIVE_SCREEN == 2:
        _spinner = 0
        GO_BACK = False
        keyboard.on_press(Voltar)

        while True:
            LitteHelp.LimparTela()
            # CHECAGEM DE ITENS -- SÓ A TELA AGORA, FAZER FUNCIONAR DEPOIS
            _spinner = (_spinner + 1) if _spinner < 3 else 0
            ScreensAndFunctions.CheckThings(_spinner, LANGUAGE)

            if GO_BACK:
                ACTIVE_SCREEN = 1
                break

            time.sleep(0.15)

    elif ACTIVE_SCREEN == 3:
        finalHTML = ScreensAndFunctions.CreateHTML(LANGUAGE)
        print('SALVANDO ARQUIVO.... LOADING BLAB BLAB BLA')
        time.sleep(0.5)

        encoded_unicode = finalHTML.encode("utf8")
        textfile = open("index.html", "wb")
        textfile.write(encoded_unicode)
        textfile.close()

        # FIM
        LitteHelp.LimparTela()
        ScreensAndFunctions.YouFinishedIt(LANGUAGE)
        ACTIVE_SCREEN = 1
        input('')

    else:
        break
