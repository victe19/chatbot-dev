from bot.src.context import Context
from typing import List

def get_entity_name(entity_list: List) -> List[str]:
    return [entity for entity in entity_list]

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
    # elif context.start == True:
    #     context = Context()

    elif intent == 'greeting' and entity_list == []:
        if entity_list == [] and context.username != None:
            action = 'ask_name'
        else:
            action = 'hello'

    elif intent == 'goodbye':
        if entity_list == []:
            action = 'goodbye'
            context.adeu = True
    
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
    
        entity_names = get_entity_name(entity_list)

        #SCHEDULE
        if "schedule" in entity_names or "degree" in entity_names or "course" in entity_names or "semester" in entity_names: 
            if context.degree != None and context.course != None and context.semester != None:
                if context.degree == "informatica" and context.course == "3" and context.mention == None:  
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
        elif "exams" in entity_names or "degree" in entity_names or "semester" in entity_names: 
                if context.degree != None and context.term != None and context.semester != None:
                    action = "exams"
                elif context.degree == None:
                    action = "ask_degree"
                elif context.term == None:
                    action = "ask_term"    
                elif context.semester == None:
                    action = "ask_semester" 
        
    
        #TEACHING_GUIDE
        elif "teaching_guide" in entity_names or "degree" in entity_names or "subject" in entity_names: 
                if context.degree != None and context.subject != None:
                    action = "teaching_guide"
                elif context.degree is None:
                    action = "ask_degree"
                elif context.subject is None:
                    action = "ask_subject"


        #TFG
        elif "tfg" in entity_names or context.tfg != None:
            if subentity_list == []:
                action = "ask_tfg"
            else:
                action = subentity_list[0][0]


        #REGISTRATION
        elif entity_list == "registration" or context.registration != None:
            if subentity_list == []:
                action = "ask_registration"
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
        

        #REGISTRATION
        elif 'registration' == entity_list or context.registration != None:
            action = "ask_registration"
        

        #CALENDAR
        elif 'calendar' == entity_list or context.calendar != None:
            action = "ask_calendar"
        

        #PERMANENCE
        elif 'permanence' == entity_list or context.permanence != None:
            action = "ask_permanence"
        

        #PROCEDURES
        elif 'procedures' == entity_list or context.procedures != None:
            action = "ask_procedures"
        

        #CREDIT_RECOGNITION
        elif 'credit_recognition' == entity_list or context.credit_recognition != None:
            action = "ask_credit_recognition"


        #COORDINATION
        elif 'coordination' == entity_list or context.coordination != None:
            action = "ask_coordination"
             
             
        #FLUX
        elif entity_list == []:
            if context.status == 'start':
                action = 'ask_start'
            if context.status == 'start_again':
                action = 'ask_start_again'

        


        

    return [action, context]


