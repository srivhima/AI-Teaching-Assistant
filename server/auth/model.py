from pydantic import BaseModel

# No need to write id field since MongoDB will automatically generate it
class StudentUser(BaseModel):
    # id: int           
    fullname:str
    email:str
    username:str
    password:str
    grade:int
    school:str


class TeacherUser(BaseModel):
    # id: int         
    fullname:str
    email:str
    username:str
    password:str
    school:str


