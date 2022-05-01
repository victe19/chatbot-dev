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
    academic = None
    exams = None
    exchange = None
    internship = None
    registration = None
    schedule = None
    teaching_guide = None
    tfg = None
    user_name: str = None
    status: str = "start"
    

    def scan_context(self) -> list:
        status_list = []
        for field in self.__dataclass_fields__:
            if field is not None:
                status_list.append(field)

        return status_list