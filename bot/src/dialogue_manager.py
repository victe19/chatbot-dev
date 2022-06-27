from contextlib import ContextDecorator
from bot.src.context import Context
from typing import List
from colorama import Fore


def get_entity_name(entity_list: List) -> List[str]:
    return [entity for entity in entity_list]


def get_status_subentity(sub_entities: List, status: str):
    status_subentity = [sub_entity for sub_entity in sub_entities if status in sub_entity[0]]
    print(f"Cleaned sub_entity {status_subentity}")
    return status_subentity[0]


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
    print(f"{Fore.CYAN}Status --> {Fore.WHITE} {context.status}")

    action = 'no_understand'

    if 'username' in entity_list:
        action = 'hello'
    elif 'language' in entity_list:
        action = 'change_language'
    
    elif entity_list == [] and subentity_list == []:
        if intent == 'greeting':
            if context.username == '':
                action = 'ask_name'
            else:
                action = 'hello'

        elif intent == 'goodbye':         
            action = 'goodbye'
            context.adeu = True

        elif intent == 'bot':
            action = 'im_bot'
        
        elif intent == 'date':
            action = 'date_today'
        
        elif intent == 'operator':
            action = 'need_operator'
        
        elif intent == 'cleverbot':
            action = 'ask_operations'

        elif intent == 'insults':
            action = 'assertive_response'
        
        elif intent == 'help':
            action = 'ask_help'
        
        elif intent == 'how_are_you':
            action = 'im_fine'

        elif intent == 'confirm':
            action = ""
        
        elif intent == 'reject':
            action = ""      

        else:
            action = 'ask_start_again'


    elif intent == 'info' or intent == None:
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
                try:
                    action = get_status_subentity(subentity_list, context.status)[0]
                except Exception as e:
                    action = 'tfg_link'


        #REGISTRATION
        elif "registration" == context.status:
            if subentity_list == []:
                action = "ask_registration"
            else:
                try:
                    action = get_status_subentity(subentity_list, context.status)[0]
                except Exception as e:
                    action = 'registration_link'


        #INTERNSHIP
        elif "internship" == context.status:
            if subentity_list == []:
                action = "ask_internship"
            else:
                try:
                    action = get_status_subentity(subentity_list, context.status)[0]
                except Exception as e:
                    action = 'internship_link'

        #ACADEMIC       
        elif "academic"  == context.status:
            action = "academic"
        

        #EXCHANGE
        elif "exchange" == context.status:
            if subentity_list == []:
                action = "ask_exchange"
            else:
                try:
                    action = get_status_subentity(subentity_list, context.status)[0]
                except Exception as e:
                    action = 'exchange_link'
        

        #CALENDAR
        elif 'calendar' == context.status:
            action = "ask_calendar"
        

        #PERMANENCE
        elif 'permanence'  == context.status:
            if subentity_list == []:
                action = "ask_permanence"
            else:
                try:
                    action = get_status_subentity(subentity_list, context.status)[0]
                except Exception as e:
                    action = 'permanence_link'
        

        #PROCEDURES
        elif 'procedures'  == context.status:
            action = "ask_procedures"
        

        #CREDIT_RECOGNITION
        elif 'credit_recognition' == context.status:
            if subentity_list == []:
                action = "ask_credit_recognition"
            else:
                try:
                    action = get_status_subentity(subentity_list, context.status)[0]
                except Exception as e:
                    action = 'credit_recognition_link'


        #COORDINATION
        elif 'coordination' == context.status:
            action = "ask_coordination"
             

        # #FLUX
        # elif entity_list == []:
        #     if context.status == 'start':
        #         action = 'ask_start'
        #     if context.status == 'start_again':
        #         action = 'ask_start_again'


    return [action, context]


