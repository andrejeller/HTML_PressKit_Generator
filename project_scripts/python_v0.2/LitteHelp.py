import os
import sys


def CheckFile(file='', spinnerInt=0) -> str:
    if not os.path.exists(file):
        return GetSpinner(spinnerInt)
    else:
        return '\033[32m OK \033[m'


def CheckRepo(pathExists, createRepo=True):
    if createRepo and (not os.path.exists(pathExists)):
        os.makedirs(pathExists)

    if not createRepo:
        return os.path.exists(pathExists)


def OnlyNumberAsInput(stringBR, stringEN, language):
    string = stringBR if language == 1 else stringEN
    while True:
        try:
            num = int(input(string))

        except (ValueError, TypeError):
            error = '(ERRO! Número inválido)' if language == 1 else '(ERROR! Invalid Number)'
            print(f'\033[0;31m{error}\033[m')

        else:
            return num  # f'{n} é um numero.'


def LimparTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def LimparUltimaLinhaEImprimir(string):
    # Só funciona no terminal, não no pyCharm
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print(string)


def PrintWithLaguage(stringBR, stringEN, language):
    string = stringBR if language == 1 else stringEN
    print(string)


def PrintWithLaguageAndGetInput(stringBR, stringEN, language):
    string = stringBR if language == 1 else stringEN
    _entry = str(input(f'{string}'))
    LimparUltimaLinhaEImprimir(f'{string}\033[32m{_entry}\033[m')
    return _entry


def GetSpinner(value=0) -> str:
    if value == 0:
        return "/"
    elif value == 1:
        return "-"
    elif value == 2:
        return "\\"
    elif value == 3:
        return "|"


def QuestionWithMultipleAnwserAndLanguage(arrayBR, arrayEN, language):
    # array = [Pergunta, Prefixo, Sufixo, Ultimo]
    texts = arrayBR if language == 1 else arrayEN

    # Print the question - How many do you want to add?
    # OLD n_for = int(input(f'{texts[0]}'))
    n_for = OnlyNumberAsInput(texts[0], texts[0], language)

    final_array = []

    # For each number to add, append on answer
    for i in range(1, n_for + 1):
        local_array = []
        print(f'{("|" if i > 1 else "")}')
        _entry = str(input(f'| {texts[1]} [{i:^3}] > {texts[2]}'))  # FOR I IN RANGE
        LimparUltimaLinhaEImprimir(f'| {texts[1]} [{i:^3}] > \033[32m{texts[2]} {_entry}\033[m')
        local_array.append(_entry)

        # If question has a link or second info on each answer
        if len(texts) > 3:
            a = 8 + len(texts[1])
            _entry = str(input(f'| {" >":>{a}} {texts[3]}'))  # <a>
            LimparUltimaLinhaEImprimir(f'| {" >":>{a}} \033[32m{texts[3]}{_entry}\033[m')
            local_array.append(_entry)

        final_array.append(local_array)

    return final_array


"""

-- OLD FUNCTIONS

def OLD_LimparUltimaLinha():
    # Só funciona no terminal, não no pyCharm
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

def OLD_QuestoesComVariasRespostas(pergunta: str, prefixo: str, sufixo: str, ultimo: str = ''):
    n_for = int(input(f'{pergunta}'))
    final_array = []
    for i in range(1, n_for + 1):
        local_array = []
        print(f'{("|" if i > 1 else "")}')
        social_name = str(input(f'| {prefixo} [{i:^3}] > {sufixo}'))  # FOR I IN RANGE

        LimparUltimaLinhaEImprimir(f'| {prefixo} [{i:^3}] > \033[32m{sufixo} {social_name}\033[m')
        local_array.append(social_name)

        if len(ultimo) > 0:
            a = 8 + len(prefixo)
            social_link = str(input(f'| {" >":>{a}} {ultimo}'))  # <a>

            LimparUltimaLinhaEImprimir(f'| {" >":>{a}} \033[32m{ultimo}{social_link}\033[m')
            local_array.append(social_link)

        final_array.append(local_array)

    return final_array
"""
