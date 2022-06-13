from bot.src.context import Context, clean_context

def get_tfg_entities() -> str:
    pass

def setup_entities(entity_list: list, context: Context()) -> list:
    Context.setup_context(context, entity_list)
    entity_name_list =  []
    for entity in entity_list:
        entity_name_list.append(entity[0])
    
    return entity_name_list


def next_action(intent: str, entity_list: list, subentity_list:list, context: Context) -> list:
    intent = intent[0] #TODO: only take first argument (name), not confidence
    entity_list = setup_entities(entity_list, context)
    action = 'no_understand'

    if 'username' in entity_list:
        action = 'hello'
    elif 'language' in entity_list:
        action = 'change_language'

    elif intent == 'greeting' and entity_list == []:
        if entity_list == [] and context.username != None:
            action = 'ask_name'
        else:
            action = 'hello'

    elif intent == 'goodbye':
        if entity_list == []:
            action = 'goodbye'
    
    elif intent == 'bot':
        if entity_list == []:
            action = 'im_bot'
    
    elif intent == 'operator':
        if entity_list == []:
            action = 'need_operator'

    elif intent == 'confirm':
        action = ""
    
    elif intent == 'reject':
        action = ""      

    elif intent == 'info' or intent == 'greeting' or intent == None:
        if entity_list == []:
            action = 'ask_start'
            context.status = 'info_more'

        # # DEGREE
        # if 'degree' in entity_list and 'course' in entity_list:
        #     action = 'ask_wich_info'

        # elif context.degree != None and context.course != None:
        #     action = 'ask_wich_info'
        
        # elif 'course' in entity_list:
        #     action = 'ask_degree'
        #     context.status = "info_more_degree"           


        #SCHEDULE
        if entity_list == "schedule" or context.schedule != None:
            if context.degree != None and context.course != None and context.semester != None:
                if context.course == "3" and context.mention == None:  
                    action = "ask_mention"
                else:
                    action = "schedule"
            elif context.degree == None:
                action = "ask_degree"
            elif context.course == None:
                action = "ask_course"      
            elif context.semester == None:
                action = "ask_semester" 
        
        #EXAMS
        if entity_list == "exams" or context.exams != None:
            if context.degree != None and context.term != None and context.semester != None:
                if context.course == "3" and context.mention != None:  
                    action = "ask_mention"
                action = "exams"
                # context = clean_context(context.username)
            elif context.degree == None:
                context.status = "info_more"
                action = "ask_degree"
            elif context.term == None:
                context.status = "info_more"
                action = "ask_term"    
            elif context.semester == None:
                context.status = "info_more"
                action = "ask_semester" 
        
        #teaching_guide
        elif 'teaching_guide' == entity_list or context.teaching_guide != None:
            if context.degree != None and context.subject != None:
                action = "teaching_guide"
            elif context.degree is None:
                action = "ask_degree"
            elif context.subject is None:
                action = "ask_subject"

        #TFG
        elif entity_list == "tfg" or context.tfg != None:
            if subentity_list == []:
                action = "ask_tfg"
            else:
                action = subentity_list[0][0]

        #INTERNSHIP
        elif entity_list == "internship" or context.internship != None:
            if subentity_list == []:
                action = "ask_internship"
            else:
                action = subentity_list[0][0]

        #ACADEMIC       
        elif entity_list == "academic" or context.academic != None:
            action = "academic"
        

        #EXCHANGE
        elif "exchange" == entity_list or context.exchange != None:
            action = "ask_exchange"
        

        #registration
        elif 'registration' == entity_list or context.registration != None:
            action = "ask_registration"
        

        #calendar
        elif 'calendar' == entity_list or context.calendar != None:
            action = "ask_calendar"
        



        #permanence
        elif 'permanence' == entity_list or context.permanence != None:
            action = "ask_permanence"
        

        #procedures
        elif 'procedures' == entity_list or context.procedures != None:
            action = "ask_procedures"
        

        #credit_recognition
        elif 'credit_recognition' == entity_list or context.credit_recognition != None:
            action = "ask_credit_recognition"


        #coordination
        elif 'coordination' == entity_list or context.coordination != None:
            action = "ask_coordination"
             

        #FLUX
        elif entity_list == []:
            if context.status == 'start':
                action = 'ask_start'
            if context.status == 'start_again':
                action = 'ask_start_again'

        


        

    return [action, context]


