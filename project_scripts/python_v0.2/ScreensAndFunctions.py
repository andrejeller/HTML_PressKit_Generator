import time
import LitteHelp
import generation_sector


def ChooseTheLanguage():
    print('ESCOLHA O IDIOMA / CHOOSE THE LANGUAGE:')
    print('[ 1 ] - PORTUGUES BRASILEIRO (PADRÃO/DEFAULT)')
    print('[ 2 ] - INTERNATIONAL ENGLISH')


def MainMenu(language):
    tam = 70

    pt_br = ['BEM VINDO AO', 'CONFERIR SE VOCÊ JÁ TEM/FEZ TUDO', 'CONFIGURAR TEXTOS / CRIAR HTML', 'SAIR']
    en_us = ['WELLCOME TO', 'CHECK IF YOU HAVE MADE EVERYTHING', 'SETUP TEXTS / CREATE HTML', 'EXIT']
    texts = pt_br if language == 1 else en_us

    print('+', '-' * tam, '+')
    print('|', f'{texts[0]:^{tam}}', '|')
    print('|', f'{"HTML PRESSKIT GENERATOR":^{tam}}', '|')
    print('+', '-' * tam, '+')
    print('')
    print(f'[{1:^3}] - {texts[1]}')
    print(f'[{2:^3}] - {texts[2]}')
    print(f'[ESC] - {texts[3]}')


def CheckThings(spinnerInt, language):
    pt_br = ['+ CONFERINDO SE VOCÊ JÁ TEM TUDO NA PASTA', '[ ESC ] - VOLTAR AO MENU +']
    en_us = ['+ CHECKING IF YOU HAVE EVERYTHING ON THE FOLDER +', '[ ESC ] - BACK TO MENU']
    texts = pt_br if language == 1 else en_us

    print('\n\n\n\n')
    print(f'{texts[0]:^{75}}', end='\n\n')

    _file = LitteHelp.CheckFile('images/favicon.png', spinnerInt)
    print(f'[{_file:^5}] - UPLOAD TO /images a FAVICON (favicon.png)')

    _file = LitteHelp.CheckFile('images/header.png', spinnerInt)
    print(f'[{_file:^5}] - UPLOAD TO /images A HEADER IMAGE (1200x240px - header.png)')

    _file = LitteHelp.CheckFile('images/img_0.png', spinnerInt)
    print(f'[{_file:^5}] - UPLOAD TO /images AT LEAST ONE IMAGE')

    _file = LitteHelp.CheckFile('images/logo_0.png', spinnerInt)
    print(f'[{_file:^5}] - UPLOAD TO /images A logo.png')
    print('')

    _file = LitteHelp.CheckFile('images/images.zip', spinnerInt)
    print(f'[{_file:^5}] - MAKE A images.zip FILE IN /images WITH THE IMAGES TO DOWNLOAD')

    _file = LitteHelp.CheckFile('images/logos.zip', spinnerInt)
    print(f'[{_file:^5}] - MAKE A logo.zip WITH IN /images WITH LOGOS VARIATIONS TO DOWNLOAD')
    print('\n')
    print(f'{texts[1]:^{75}}')


def CreateHTML(language) -> str:
    pt_br = [' INFORMAÇÕES BÁSICAS ', ' PARTE DA HISTÓRIA ', ' RECURSOS VISUAIS ', ' PRÊMIOS E RECONHECIMENTO ', ' SELECTED ARTICLES / (Frases) ', ' MEMBROS DA EQUIPE ']
    en_us = [' BASIC INFO ', ' HISTORY PART ', ' VISUAL RESOURCES ', ' AWARDS & RECOGNITION ', ' SELECTED ARTICLES ', ' TEAM MEMBERS ']
    texts = pt_br if language == 1 else en_us

    # PREENCHER O FORMULARIO PARA CRIAR ARQUIVO HTML
    finalHTML = ""

    # ------------------------
    # 01 INFORMAÇÕES BÁSICAS
    LitteHelp.LimparTela()
    print(f'{texts[0]:=^70}')
    _pageTitle = LitteHelp.PrintWithLaguageAndGetInput('TÍTULO DA PÁGINA HTML:  ', 'HTML PAGE TITLE:  ', language)
    _companyName = LitteHelp.PrintWithLaguageAndGetInput('NOME DA EMPRESA OU JOGO:  ', 'COMPANY/GAME NAME:  ', language)
    _companyWebSite = LitteHelp.PrintWithLaguageAndGetInput('WEBSITE:  ', 'WEBSITE:  ', language)
    _companyDescription = LitteHelp.PrintWithLaguageAndGetInput('DESCRIÇÃO:  ', 'DESCRIPTION:  ', language)
    _developer = LitteHelp.PrintWithLaguageAndGetInput('DESENVOLVEDOR:  ', 'DEVELOPER:  ', language)
    _developerLink = LitteHelp.PrintWithLaguageAndGetInput('LINK DO DESENVOLVEDOR:  ', 'DEVELOPER LINK:  ', language)
    _basedIn = LitteHelp.PrintWithLaguageAndGetInput('SEDE EM:  ', 'BASED IN:  ', language)
    _foundingDate = LitteHelp.PrintWithLaguageAndGetInput('DATA DE FUNDAÇÃO:  ', 'FOUNDING DATE:  ', language)
    _adress = LitteHelp.PrintWithLaguageAndGetInput('ENDEREÇO:  ', 'ADDRESS:  ', language)
    _email = LitteHelp.PrintWithLaguageAndGetInput('EMAIL DE CONTATO (PRESS):  ', 'CONTACT E-MAIL (PRESS):  ', language)
    _phone = LitteHelp.PrintWithLaguageAndGetInput('TELEFONE DE CONTATO:  ', 'CONTACT PHONE:  ', language)

    # ------------------------
    # 02 - INFORMAÇÕES BASICAS
    LitteHelp.LimparTela()
    print(f'{texts[0]:=^70}')
    # _social = LitteHelp.QuestoesComVariasRespostas('NÚmero de Redes Sociais para adicionar: ', 'Rede', 'Nome: ', 'Link: https://www.')
    _ptBr = ['Número de Redes Sociais para adicionar: ', 'Rede', 'Nome: ', 'Link: https://www.']
    _enUs = ['Number of Social Networks to Add: ', 'Networks', 'Name: ', 'Link: https://www.']
    _social = LitteHelp.QuestionWithMultipleAnwserAndLanguage(_ptBr, _enUs, language)

    # ------------------------
    # 03 - HISTORY PART
    LitteHelp.LimparTela()
    print(f'{texts[1]:=^70}')
    _earlyHistory = str(input('História inicial: '))
    _afterThat = str(input('Depois disso: '))

    _ptBr = ['Número de Projetos para adicionar (com Link): ', 'Projeto', 'Nome: ', 'Link: https://www.']
    _enUs = ['Number of Projects to Add (with Link): ', 'Project', 'Name: ', 'Link: https://www.']
    _projects = LitteHelp.QuestionWithMultipleAnwserAndLanguage(_ptBr, _enUs, language)

    # ------------------------
    # 04 - RECURSOS VISUAIS
    LitteHelp.LimparTela()
    print(f'{texts[2]:=^70}')

    _ptBr = ['Número de Vídeos para adicionar (com Link): ', 'Vídeo', 'Comentário: ', 'Link: https://www.']
    _enUs = ['Number of Videos to Add (with Link): ', 'Video', 'Coment: ', 'Link: https://www.']
    _videos = LitteHelp.QuestionWithMultipleAnwserAndLanguage(_ptBr, _enUs, language)

    print('')
    # OLD _imagesCount = int(input('Número de IMAGENS que voê deseja adicionar: '))
    _imagesCount = LitteHelp.OnlyNumberAsInput('Número de IMAGENS que voê deseja adicionar:', 'Number of IMAGES you want to Add:', language)
    # print('[LEMBRE DE RENOMEAR AS IMAGENS COMO img_0, img_1, img_2, ...]')
    LitteHelp.PrintWithLaguage('[LEMBRE DE RENOMEAR AS IMAGENS COMO img_0, img_1, img_2, ...]', '[REMEMBER TO RENAME THE IMAGES AS img_0, img_1, img_2, ...]', language)

    print('')
    # OLD _logoCount = int(input('Número de LOGOS que voê deseja adicionar: '))
    _logoCount = LitteHelp.OnlyNumberAsInput('Número de LOGOS que voê deseja adicionar:', 'Number of VIDEOS you want to Add:', language)
    # print('[LEMBRE DE RENOMEAR AS LOGOS COMO logo_0, logo_1, logo_2, ...]')
    LitteHelp.PrintWithLaguage('[LEMBRE DE RENOMEAR AS LOGOS COMO logo_0, logo_1, logo_2, ...]', '[REMEMBER TO RENAME THE LOGOS AS logo_0, logo_1, logo_2, ...]', language)

    # ------------------------
    # 05 - AWARDS & RECOGNITION / PRÊMIOS E RECONHECIMENTO
    LitteHelp.LimparTela()
    print(f'{texts[3]:=^70}')
    _ptBr = ['Número de PRÊMIOS/RECONHECIMENTOS que voê deseja adicionar: ', 'Prêmio', 'Comentário: ']
    _enUs = ['Number of Awards you want to Add: ', 'Awards', 'Coment: ']
    _awards = LitteHelp.QuestionWithMultipleAnwserAndLanguage(_ptBr, _enUs, language)

    # ------------------------
    # 06 - SELECTED ARTICLES / "ARTIGOS" Relacionados -- mais para "frases de impacto/ que gosta"
    LitteHelp.LimparTela()
    print(f'{texts[4]:=^70}')
    _ptBr = ['Número de ARTIGOS que voê deseja adicionar: ', 'Frase', 'Comentário: ', 'Autor: ']
    _enUs = ['Number of Articles you want to Add: ', 'Article', 'Coment: ', 'Author: ']
    _articles = LitteHelp.QuestionWithMultipleAnwserAndLanguage(_ptBr, _enUs, language)

    # ------------------------
    # 07 -TEAM MEMBERS
    LitteHelp.LimparTela()
    print(f'{texts[5]:=^70}')
    _ptBr = ['Número de MEMBROS que voê deseja adicionar ao seu TIME: ', 'Membro', 'Nome: ', 'Função: ']
    _enUs = ['Number of MEMBERS you want to Add to your TEAM: ', 'Member', 'Name: ', 'Function: ']
    _team = LitteHelp.QuestionWithMultipleAnwserAndLanguage(_ptBr, _enUs, language)

    LitteHelp.LimparTela()
    print('GERANDO HTML.... LOADING BLAB BLAB BLA')
    time.sleep(1.0)

    finalHTML += generation_sector.GetHeader(_pageTitle)
    finalHTML += generation_sector.GetLeftBar(_companyName, _companyWebSite, language)
    finalHTML += generation_sector.GetFactSheet(_developer, _developerLink, _basedIn, _foundingDate, _developerLink, _email, language)
    finalHTML += generation_sector.GetFactSheet_SocialAndProjects(_social, _projects, language)
    finalHTML += generation_sector.GetFactSheet_AddressAndPhone(_adress, _phone, language)
    finalHTML += generation_sector.GetDescriptionAndHistory(_companyDescription, _earlyHistory, _afterThat, _projects, language)
    finalHTML += generation_sector.GetVisualResources(_videos, _imagesCount, _logoCount, _companyName, _email, language)
    finalHTML += generation_sector.GetAwardsAndArticles(_awards, _articles, language)
    finalHTML += generation_sector.GetTeamAndcontact(_team, _email, _social, _companyWebSite, language)
    finalHTML += generation_sector.GetFinals(language)
    # print(finalHTML)

    return finalHTML


def YouFinishedIt(language):
    tam = 70

    pt_br = ['VOCE TERMINOU O SETUP', 'VEJA NO MENU SE ESQUECEU DE ALGO', '[ ENTER ] - Voltar ao Menu']
    en_us = ['YOU FINISH THE SETUP', 'CHECK IF YOU FORGOT SOMETHING', '[ ENTER ] - Back to Menu']
    texts = pt_br if language == 1 else en_us

    print('+', '-' * tam, '+')
    print('|', f'{texts[0]:^{tam}}', '|')
    print('|', f'{texts[1]:^{tam}}', '|')
    print('+', '-' * tam, '+')
    print('')
    print(f'{texts[2]:^{75}}')
