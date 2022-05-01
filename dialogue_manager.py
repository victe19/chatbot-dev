from context import Context

def next_action(intent: str, entity_list: list, context: Context) -> list:
    # context = Context.scan_context(context)
    intent = intent[0]
    action = None

    if intent == None:
        if entity_list == []:
            action = 'ask_degree'
            context.status = 'start'

        elif ("degree", "química") in entity_list:
            action = 'ask_course'
            context.status = "info_more_degree"
    
            
    elif intent == 'greeting':
        if entity_list == []:
            action = 'hello'
        elif 'user_name' in entity_list:
            action = 'hello'
            #TODO context.user_name = 
    
    elif intent == 'info':
        if entity_list == []:
            action = 'ask_degree'
            context.status = 'info_more'

        elif 'academic' in entity_list:
            action = 'academic'
            context.academic = True

        elif 'tfg' in entity_list and 'teaching_guide' in entity_list:
            action = 'tfg_teaching_guide'
            context.tfg = True
            context.teaching_guide = True
    
    return [action, context]
