from dataclasses import dataclass


@dataclass
class Context:
    course: str = None
    degree:str = None
    department: str = None
    mencion: str = None
    professor: str = None
    semester: int = None
    year: int = None
    academic: bool = None
    exams: bool = None
    exchange: bool = None
    internship: bool = None
    registration: bool = None
    schedule: bool = None
    teaching_guide: bool = None
    tfg: bool = None
    username: str = ""
    status: str = "start"


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


