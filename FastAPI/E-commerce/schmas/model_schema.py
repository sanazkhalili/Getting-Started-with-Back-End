from pydantic import BaseModel, validator, FilePath
import datetime



#برای چک کردن مقادیر  validate  کردن



class UserBaseSchema(BaseModel):
    username : str
    email : str
    join_data : datetime.date
    
    class Config():
        orm_mode=True


class UserCreate(UserBaseSchema):
    password : str
    is_verified : bool
    

class BusinessBase(BaseModel):
    business_name: str
    city: str
    region: str
    business_description: str
    logo: str

    class Config():
        orm_model = True
    
    @validator('business_name')
    def validate_business_name(cls, business_name):
        if not business_name:
            raise ValueError("Business name cannot be empty sanaz.")
        return business_name


