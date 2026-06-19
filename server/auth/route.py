from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .model import StudentUser, TeacherUser
from config.db import users_collection
from .hash_utils import hash_password, verify_password


router = APIRouter()
security = HTTPBasic()

# def authenticate(credentials:HTTPBasicCredentials=Depends(security)):
#     """Authenticate a user using HTTP Basic Auth"""
#     user= users_collection.find_one({"username":credentials.username})
#     if not user or not verify_password(credentials.password, user.get("password")):
#         raise HTTPException(status_code=401, detail="Invalid username or password")
#     # return credentials.username
#     #if you want to return full details
#     return {
#         "username":user.get("username"),
#         "role": user.get("role"),
#         "grade":user.get("grade"),
#         "user_id":str(user.get("_id"))
#     }

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):

    try:
        print("Searching:", credentials.username)

        user = users_collection.find_one({
            "username": credentials.username
        })

        print("Mongo Result:", user)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        if not verify_password(
            credentials.password,
            user.get("password")
        ):
            raise HTTPException(
                status_code=401,
                detail="Wrong password"
            )

        return {
            "username": user["username"],
            "role": user["role"],
            **({"grade": user["grade"]} if "grade" in user else {}),
            "user_id": str(user["_id"])
        }

    except Exception as e:
        print("LOGIN ERROR:", str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )






@router.post("/signup/student")
def signup_student(req: StudentUser):
    """Handle a student signup request."""

    # check if username already exists 
    if users_collection.find_one({"username":req.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # hash the password before storing
    hashed_passsword = hash_password(req.password)
    users_collection.insert_one({
        "fullname": req.fullname,
        "email": req.email,
        "username": req.username,
        "password": hashed_passsword,
        "role": "Student",
        "grade": req.grade,
        "school": req.school,
    })

    return {"message": "Student user created successfully"}



@router.post("/signup/teacher")
def signup_teacher(req: TeacherUser):
    """Handle a teacher signup request."""

    # check if username already exists 
    if users_collection.find_one({"username":req.username}):
        raise HTTPException(status_code=400, detail="Teacher name already exists")
    
    # hash the password before storing
    hashed_passsword = hash_password(req.password)
    users_collection.insert_one({
        "fullname": req.fullname,
        "email": req.email,
        "username": req.username,
        "password": hashed_passsword,
        "role": "Teacher",
        "school": req.school,
    })

    return {"message": "Teacher user created successfully"}


@router.get("/login")
def login(user=Depends(authenticate)):
    """Handles user login"""
    return {"message":f"Welcome {user['username']}","role":user["role"]}
