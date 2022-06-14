from dataclasses import dataclass
from multiprocessing import context


@dataclass
class Context:
    adeu: bool = False
    academic: bool = None
    calendar: bool = None
    coordination: bool = None
    course: str = None
    credit_recognition: bool = None
    degree:str = None
    department: str = None
    exams: bool = None
    exchange: bool = None
    internship: bool = None
    language: str = 'cat'
    mention: str = None
    permanence: bool = None
    procedures: bool = None
    professor: str = None
    registration: bool = None
    schedule: bool = None
    semester: int = None
    teaching_guide: bool = None
    term: str = None
    tfg: bool = None
    username: str = ""
    subject: str = None
    year: int = None
    status: str = "start"
    start: bool = False


    def setup_context(self, entity_list):
        dataclass_fields = list(self.__dataclass_fields__.keys())

        for entity in entity_list:
            entity_name, entity_value = entity
            if entity_name in dataclass_fields:
                setattr(self, entity_name, entity_value)


    def scan_context(self) -> list:
        status_list = []
        for field in self.__dataclass_fields__:
            if field is not None:
                status_list.append(field)

        return status_list
    

def clean_context(name: str, status: str = "start_again") -> Context:
    context = Context()
    context.username = name
    context.status = status
    return context



