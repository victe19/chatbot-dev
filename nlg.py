from context import Context

def generate(action: str, context: Context()) -> str:    
    response = "Ho sento, no t'he entès. Podríes repetir?"
    context.user_name = "Victor"
    
    if action == 'hello':
        response = f"Hola, {context.user_name}, encantat de saludar-te. Com et puc ajudar?"
    
    elif action == 'ask_degree':
        response = f"D'acord, {context.user_name}, em podries indicar de quin grau/carrera?"
    
    elif action == 'ask_course':
        response = f"D'acord, {context.user_name}, em podries indicar de quin curs?"
    
    elif action == 'tfg_teaching_guide':
        response = f"Mira, {context.user_name}, en aquest enllaç podràs trobar la guia docent que em demanes"    

    return response
    