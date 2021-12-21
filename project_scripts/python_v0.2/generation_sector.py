# std::ofstream myfile;
# myfile.open("./" + fileName);

def GetHeader(PageTitle) -> str:
    return f"""<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name='viewport' content='width = device-width, initial-scale = 1, shrink-to-fit = no'>
            
            <!-- Bootstrap CSS -->
            <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css' integrity='sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO' crossorigin='anonymous'>
            <link rel='stylesheet' href='http://www.andrejeller.com/HTML_PressKit_Generator/css/originalDoPressKit.css'>
            
            
            <title> {PageTitle} </title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <link rel='shortcut icon' href='images/favicon.png'>
        </head>"""


def GetLeftBar(CompanyName, CompanyWebSite, language) -> str:
    en_us = ['Factsheet', 'Description', 'History', 'Projects', 'Videos', 'Images', 'Logo & Icon', 'Awards & Recognition', 'Selected Articles', 'Team', 'Contact']
    pt_br = ['Factsheet', 'Descrição', 'História', 'Projetos', 'Vídeos', 'Imagens', 'Logos & Icones', 'Prêmios e Reconhecimentos', 'Artigos Selecionados', 'Equipe', 'Contato']
    texts = pt_br if language == 1 else en_us

    return f"""
        <body>
            <div class='container'>
                <div class='row'>
                    <!-- LEFT NAVBAR -->
                    <div class='col col-lg-3  p-3 mb-2 bg-white text-dark' style='font-family:Trebuchet MS; '>
                        <p class='h2' style='font-family:Trebuchet MS; '>{CompanyName}</p>
                        <a href='https://www.{CompanyWebSite}' target='_blank'>{CompanyWebSite}</a>
                        
                        <br><br>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#factsheet'>{texts[0]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#description'>{texts[1]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#history'>{texts[2]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#projects'>{texts[3]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#videos'>{texts[4]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#images'>{texts[5]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#logo'>{texts[6]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#awards'>{texts[7]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#articles'>{texts[8]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#credits'>{texts[9]}</a>
                        <a class='btn btn-light btn-sm btn-block text-left' href='#contact'>{texts[10]}</a>
                    </div>"""


def GetFactSheet(Developer, DeveloperLink, BasedIn, FoundingDate, Website, PressContactEmail, language) -> str:
    en_us = ['Factsheet', 'Developer', 'Based in', 'Founding date', 'Website', 'Press / Business contact']
    pt_br = ['Factsheet', 'Desenvolvedor', 'Com sede em', 'Data de fundação', 'Website', 'Contato Imprensa / Comercial']
    texts = pt_br if language == 1 else en_us

    return f""" <!--  FACTSHEET -->
                    <div class='col-sm' style='font-family:Trebuchet MS;'>
                        <img src='images/header.png' class='img-fluid' alt='Responsive image'>
                        <div class='row'>
                            <div class='col col-lg-4'>
                                <br><p class='h3' style='font-family:Georgia; 'id='factsheet'>{texts[0]}</p>
                                
                                <br><p class='font-weight-normal' >
                                <strong> {texts[1]}: </strong><br>
                                <a href='https://www.{DeveloperLink}'> {Developer} </a> <br>
                                {texts[2]} {BasedIn}
                                </p>
                                
                                <p class='font-weight-normal'>
                                <strong> {texts[3]}: </strong><br>
                                {FoundingDate} 
                                </p>

                                <p class='font-weight-normal'>
                                <strong> {texts[4]}: </strong><br>
                                <a href='https://www.{Website}' target='_blank'> https://www.{Website} </a>
                                <p>

                                <p class='font-weight-normal'>
                                <strong> {texts[5]}: </strong><br>
                                <a href='mailto:{PressContactEmail}'>{PressContactEmail}</a>
                                <p> """


def GetFactSheet_SocialAndProjects(SocialsArray, ProjectsArray, language) -> str:
    en_us = ['Social', 'Releases']
    pt_br = ['Redes Sociais', 'Lançamentos']
    texts = pt_br if language == 1 else en_us

    toReturn = f"""
                                <p class='font-weight-normal'>
                                    <strong> {texts[0]}: </strong> <br>"""

    for social in SocialsArray:
        toReturn += f""" 
                                    <a href='https://www.{social[1]}' target='_blank'> {social[0]} </a> <br>"""

    toReturn += f"""
                                </p>
                                
                                <p class='font-weight-normal'>
                                    <strong> {texts[1]}: </strong> <br> <!-- Criar presskit para os games bons-->"""

    for project in ProjectsArray:
        toReturn += f""" 
                                    <a href='{project[1]}' target='_blank'> {project[0]} </a> <br>"""

    toReturn += """
                                </p>"""

    return toReturn


def GetFactSheet_AddressAndPhone(Address, Phone, language) -> str:
    en_us = ['Address', 'Phone']
    pt_br = ['Endereço', 'Telefone']
    texts = pt_br if language == 1 else en_us

    return f""" 
                                
                                <p class='font-weight-normal' >
                                    <strong> {texts[0]}: </strong> <br>
                                    {Address}
                                </p>

                                <p class='font-weight-normal'>
                                    <strong> {texts[1]}: </strong> <br>
                                    {Phone}
                                </p>
                            </div>"""


def GetDescriptionAndHistory(Description, EarlyHistory, AfterThat, ProjectsArray, language) -> str:
    en_us = ['Description', 'History', 'Early history', 'After that', 'Projects']
    pt_br = ['Descrição', 'História', 'História inicial', 'Depois disso', 'Projetos']
    texts = pt_br if language == 1 else en_us

    #  DESCRICAO
    toReturn = f"""
                            
                            <div class='col-sm'>
                                <br>
                                <p class='h3' style='font-family:Georgia;' id='description'> {texts[0]} </p>
                                <p> {Description} </p>
                                
                                <br>
                                <p class='h4' style='font-family:Georgia;' id='history'> {texts[1]} </p>
                                <p class='font-weight-bold'> {texts[2]} </p>
                                <p> {EarlyHistory} </p>
                                
                                <br>
                                <p class='font-weight-bold'> {texts[3]}</p>
                                <p> {AfterThat} </p>
                                
                                <br>
                                <p class='h3' style='font-family:Georgia;' id='projects'> {texts[4]} </p>"""

    for project in ProjectsArray:
        toReturn += f""" 
					            &emsp; &middot; <a href='https://www.{project[1]}' target='_blank'>{project[0]}</a> <br> """

    toReturn += """
                            </div>
                        </div>"""

    return toReturn


def GetVisualResources(VideosArray, ImagesCount, LogosCount, Empresa, Email, language) -> str:
    en_us = ['Videos', 'Images', 'Logos & Icons']
    pt_br = ['Vídeos', 'Imagens', 'Logos & Icones']
    texts = pt_br if language == 1 else en_us

    # VIDEOS
    toReturn = f"""
                        <hr>
                        <br><p class='h3' style='font-family:Georgia;' id='videos'> {texts[0]} </p>
    """
    for video in VideosArray:
        toReturn += f"""
                        <p class='font-italic'> {video[0]} <a href='https://www.{video[1]}' target='_blank'> Youtube </a> </p>
                        <iframe width=100% height='315' src='https://www.{video[1]}' frameborder='0' allow='autoplay; encrypted-media' allowfullscreen></iframe>
                """

    # IMAGES
    toReturn += f"""
                        <hr>
                        <br><p class='h3' style='font-family:Georgia;' id='images'>{texts[1]}</p>
                        <div class='alert alert alert-primary' role='alert'>
                            <a href='images/images.zip'>download all screenshots & photos as .zip(2 MB)</a>
                        </div>
                        <picture> """

    for i in range(0, ImagesCount):
        if i % 2 == 0:
            toReturn += f"""
                            <img src='images/img_{i}.png' class='rounded img-fluimages/id' width=48.7%> """
        else:
            toReturn += f"""
                            <img src='images/img_{i}.png' class='rounded img-fluimages/id float-right' width=48.7%>
                            <br><br> """

    toReturn += f"""
                        </picture>
                        <br><br>
                        <p>
                            Existem muito mais imagens disponíveis para {Empresa}, mas estas são as que achamos que seriam mais úteis para você. Se você tiver solicitações específicas, por favor
                            <a href='mailto:{Email}' target='_blank'>Faça Contato!</a>
                        </p>"""

    # LOGOS
    toReturn += f"""
                        <hr>
                        <br><p class='h3' style='font-family:Georgia;' id='logo'>{texts[2]}</p>
                        <div class='alert alert alert-primary' role='alert'>
                            <a href='images/logo.zip'>download logo files as .zip(1 MB)</a>
                        </div>
                        <picture> """

    for i in range(0, LogosCount):
        if i % 2 == 0:
            toReturn += f"""
                            <img src='images/logo_{i}.png' class='rounded img-fluimages/id' width=48.7%> """
        else:
            toReturn += f"""
                            <img src='images/logo_{i}.png' class='rounded img-fluimages/id float-right' width=48.7%>
                            <br><br> """

    toReturn += f"""
                        </picture>
                        </p> """

    return toReturn


def GetAwardsAndArticles(AwardsArray, ArticlesArray, language) -> str:
    en_us = ['Awards & Recognition', 'Selected Articles']
    pt_br = ['Prêmios e Reconhecimentos', 'Artigos Selecionados']
    texts = pt_br if language == 1 else en_us

    # AWARDS
    toReturn = f"""
                        <hr>
                        <br><p class='h3' style='font-family:Georgia;' id='awards'>{texts[0]}</p> """

    for award in AwardsArray:
        toReturn += f""" 
                        <p> &middot; {award[0]} </p>"""

    # SELECTED ARTICLES
    toReturn += f"""
                        <hr>
                        <br><p class='h3' style='font-family:Georgia;' id='articles'>{texts[1]}</p> """

    for article in ArticlesArray:
        toReturn += f""" 
                        <p> &middot; '{article[0]}'<br> &emsp; - {article[1]}</p> """

    return toReturn


def GetTeamAndcontact(TeamArray, PressContactEmail, SocialArray, Website, language) -> str:
    en_us = ['Team & Repeating Collaborator', 'Contact']
    pt_br = ['Equipe', 'Contato']
    texts = pt_br if language == 1 else en_us

    # TEAM
    toReturn = f"""
                        <hr>
                        <div class='row'>
                            <div class='col col-lg-6'>
                                <br><p class='h3' style='font-family:Georgia;' id='credits'>{texts[0]}</p>
                                 """

    for member in TeamArray:
        toReturn += f""" 
                                <p> {member[0]} <br> {member[1]} </p> """

    # CONTACT
    toReturn += f"""
                            </div>
                            <div class='col-sm'>
                                <br><p class='h3' style='font-family:Georgia;' id='contact'>{texts[1]}</p>
                                <p>Inquiries<br>
                                <a href='mailto:{PressContactEmail}'> {PressContactEmail} </a></p> """

    for contact in SocialArray:
        toReturn += f""" 
                                <p> {contact[0]} <br>
                                <a href='https://www.{contact[1]}' target='_blank'> {contact[1]} </a></p> """

    toReturn += f"""
                                <p>Web<br>
                                <a href='https://www.{Website}' target='_blank'> {Website} </a></p>
                            </div>
                        </div> """

    return toReturn


def GetFinals(language) -> str:
    pt_br = """Feito com *HTMLPressKitGenerator* criado por Andre Jeller <a href='https://www.andrejeller.com' target='_blank1'>(AJS)</a> - usando <a href='http://dopresskit.com/' target='_blank'>DoPresskit()</a> como modelo."""
    en_us = """Done with *HTMLPressKitGenerator* created by Andre Jeller <a href='https://www.andrejeller.com' target='_blank1'>(AJS)</a> - using <a href='http://dopresskit.com/' target='_blank'>DoPresskit()</a> as model."""
    texts = pt_br if language == 1 else en_us

    toReturn = f"""
                        <hr> 
                        <p> {texts} </p>
                    </div>
                </div>
            </div>
        </body>
    </html>"""

    return toReturn
