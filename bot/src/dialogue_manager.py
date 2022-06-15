from contextlib import ContextDecorator
from bot.src.context import Context
from typing import List

def get_entity_name(entity_list: List) -> List[str]:
    return [entity for entity in entity_list]

def setup_entities(entity_list: List, context: Context()) -> List:
    Context.setup_context(context, entity_list)
    entity_name_list =  []
    for entity in entity_list:
        entity_name_list.append(entity[0])
    
    return entity_name_list


def next_action(intent: str, entity_list: list, subentity_list:list, context: Context()) -> list:
    intent = intent[0] #TODO: only take first argument (name), not confidence
    entity_list = setup_entities(entity_list, context)
    context.setup_status(entity_list)
    print(f"Status --> {context.status}")

    action = 'no_understand'

    if 'username' in entity_list:
        action = 'hello'
    elif 'language' in entity_list:
        action = 'change_language'
    # elif context.start == True:
    #     context = Context()

    elif intent == 'greeting' and entity_list == [] and context.status == 'start':
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
        if entity_list == [] and subentity_list == []:
            action = 'ask_start'
    
        #SCHEDULE
        if "schedule" == context.status:
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
        elif "exams" == context.status: #or "degree" in entity_names or "semester" in entity_names: 
                if context.degree != None and context.term != None and context.semester != None:
                    action = "exams"
                elif context.degree == None:
                    action = "ask_degree"
                elif context.term == None:
                    action = "ask_term"    
                elif context.semester == None:
                    action = "ask_semester" 
        
    
        #TEACHING_GUIDE
        elif "teaching_guide" == context.status: #or "degree" in entity_names or "subject" in entity_names: 
                if context.degree != None and context.subject != None:
                    action = "teaching_guide"
                elif context.degree is None:
                    action = "ask_degree"
                elif context.subject is None:
                    action = "ask_subject"


        #TFG
        elif "tfg" == context.status:
            if subentity_list == []:
                action = "ask_tfg"
            else:
                action = subentity_list[0][0]


        #REGISTRATION
        elif "registration" == context.status:
            if subentity_list == []:
                action = "ask_registration"
            else:
                action = subentity_list[0][0]


        #INTERNSHIP
        elif "internship" == context.status:
            if subentity_list == []:
                action = "ask_internship"
            else:
                action = subentity_list[0][0]


        #ACADEMIC       
        elif "academic"  == context.status:
            action = "academic"
        

        #EXCHANGE
        elif "exchange" == context.status:
            action = "ask_exchange"
        

        #REGISTRATION
        elif 'registration'  == context.status:
            action = "ask_registration"
        

        #CALENDAR
        elif 'calendar' == context.status:
            action = "ask_calendar"
        

        #PERMANENCE
        elif 'permanence'  == context.status:
            action = "ask_permanence"
        

        #PROCEDURES
        elif 'procedures'  == context.status:
            action = "ask_procedures"
        

        #CREDIT_RECOGNITION
        elif 'credit_recognition' == context.status:
            action = "ask_credit_recognition"


        #COORDINATION
        elif 'coordination' == context.status:
            action = "ask_coordination"
             

        #FLUX
        elif entity_list == []:
            if context.status == 'start':
                action = 'ask_start'
            if context.status == 'start_again':
                action = 'ask_start_again'


    return [action, context]


