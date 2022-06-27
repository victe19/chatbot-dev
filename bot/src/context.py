from dataclasses import dataclass
from multiprocessing import context

DYNAMIC_STATUS = ["academic", "calendar", "coordination", "credit_recognition", "exams", "exchange", "internship", "permanence", "procedures", "registration", "schedule", "teaching_guide", "tfg"]

@dataclass
class Context:
    course: str = None
    degree:str = None
    department: str = None
    language: str = 'cat'
    mention: str = None
    professor: str = None
    semester: int = None
    status: str = "start"
    prevstatus: str = "start"
    subject: str = None
    term: str = None
    username: str = ""
    year: int = None
    
    adeu: bool = False
    start: bool = False


    def setup_status(self, entity_list):

        if entity_list:
            for entity in entity_list:
                if entity in DYNAMIC_STATUS:
                    self.status = entity 

    
    def setup_context(self, entity_list):
        dataclass_fields = list(self.__dataclass_fields__.keys())

        for entity in entity_list:
            entity_name, entity_value = entity
            if entity_name in dataclass_fields:
                setattr(self, entity_name, entity_value)
        if self.username:
            self.username = self.username.capitalize()




