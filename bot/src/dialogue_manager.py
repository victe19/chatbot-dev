from bot.src.context import Context

def next_action(intent: str, entity_list: list, context: Context) -> list:
    intent = intent[0] #TODO: only take first argument (name), not confidence
    entity_list = setup_entities(entity_list, context)
    action = None


    if intent == 'greeting':
        if entity_list == [] and context.username != None:
            action = 'ask_name'
        elif 'username' in entity_list:
            action = 'hello'
    
    elif intent == 'bot':
        if entity_list == []:
            action = 'im_bot'
    
    elif intent == 'operator':
        if entity_list == []:
            action = 'need_operator'      


    elif intent == 'info' or intent == None:
        if entity_list == []:
            action = 'ask_start'
            context.status = 'info_more'

        # DEGREE
        elif 'degree' in entity_list and 'course' in entity_list:
            action = 'ask_wich_info'

        elif context.degree != None and context.course != None:
            action = 'ask_wich_info'

        elif 'degree' in entity_list:
            action = 'ask_course'
            context.status = "info_more_degree"
        
        elif 'course' in entity_list:
            action = 'ask_degree'
            context.status = "info_more_degree"    

        # EXPEDIENT
        elif 'academic' in entity_list:
            action = 'academic'        

        #TFG
        elif 'tfg' in entity_list and 'teaching_guide' in entity_list:
            action = 'tfg_teaching_guide'
        
        elif 'tfg' in entity_list:
            action = 'tfg'

        elif 'username' in entity_list:
            action = 'ask_start'

        elif entity_list == "shedule":
            if context.degree != None and context.course != None and context.semester != None:
                if context.course == "3" and context.mention != None:  
                    action = "ask_mention"
                action = context.degree + "_" + context.course + "_" + context.semester + "_shedule"
            elif context.degree != None:
                action = "ask_degree"
            elif context.course != None:
                action = "ask_course"      
            elif context.semester != None:
                action = "ask_semester"     

        elif entity_list == []:
            action = 'ask_start'
            context.status = 'start'
        
    
    return [action, context]


def setup_entities(entity_list: list, context: Context()) -> list:
        Context.setup_context(context, entity_list)
        entity_name_list =  []
        for entity in entity_list:
            entity_name_list.append(entity[0])
        
        return entity_name_list
