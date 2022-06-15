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
    subject: str = None
    term: str = None
    username: str = ""
    year: int = None
    
    adeu: bool = False
    start: bool = False


    def setup_status(self, entity_list):
        # dataclass_fields = list(self.__dataclass_fields__.keys())
        # print(f"Fields --> {type(dataclass_fields[0])}")

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


    def scan_context(self) -> list:
        status_list = []
        for field in self.__dataclass_fields__:
            if field is not None:
                status_list.append(field)

        return status_list


    def clean_context(self, context_list):
        print(f"Cleaning Context for {context_list} . . . ")
        for name in context_list:
            print(name)
            self.name = None
        return self
        

    def reset_context(self, name: str, status: str = "start_again"):
        self = Context()
        self.username = name
        self.status = status




