from src.context import Context

def generate(action: str, context: Context()) -> str:    
    response = "Ho sento, no t'he entès. Podríes repetir?"
    
    if action == 'hello':
        response = f"Hola, {context.username}, encantat de saludar-te. Com et puc ajudar?"
    
    elif action == 'ask_name':
        response = f"Hola, encantat de saludar-te. Primer de tot, com em puc dirigir a tu?"
    
    elif action == 'ask_start':
        response = f"Encantat, {context.username}, em podries indicar en què et puc ajudar?"

    elif action == 'ask_degree':
        response = f"D'acord, {context.username}, em podries indicar de quin grau/carrera?"
    
    elif action == 'ask_course':
        response = f"D'acord, {context.username}, em podries indicar de quin curs?"
    
    elif action == 'ask_wich_info':
        response = f"D'acord, {context.username}, de què t'agraderia tenir més informació?"
    
    elif action == 'tfg':
        response = f"Si, {context.username} El TFG és un treball que recopila tots els coneixaments englobats dins el teu grau"

    elif action == 'tfg_teaching_guide':
        response = f"Mira, {context.username}, en aquest enllaç podràs trobar la guia docent que em demanes"    
    
    elif action == 'academic':
        response = f"Per tal de consultar el teu expedient acadèmic, {context.username}, pots entrar al SIA amb el teu usuari i contrasenya en el següent enllaç"    
    
    elif action == 'im_bot':
        response = f"Per tal de consultar el teu expedient acadèmic, {context.username}, pots entrar al SIA amb el teu usuari i contrasenya en el següent enllaç"    
    
    elif action == 'need_operator':
        response = f"Si necessites posar-te en contacte amb una persona de l'escola, {context.username}, pots trucar al telèfon següent o escriure al correu@enginyeria.cat"    

    return response
    