from fastapi import APIRouter, Depends, HTTPException
from models import model
from dependence import get_db
from sqlalchemy.orm import Session
from schmas import model_schema
from schmas import crud
from fastapi import File, UploadFile
from typing import Union
from PIL import Image
from fastapi.responses import StreamingResponse
import numpy as np
from io import BytesIO
import base64 

router = APIRouter()

@router.get('/add_user')
def add_test(db:Session=Depends(get_db)):
    return "tetst"


@router.post('/create_user')
def add_user(user:model_schema.UserCreate , db:Session=Depends(get_db)):
    new_user = model.User(**vars(user))
    user1, user2 = crud.get_user(db, user.username, user.email)
    if user1 or user2:
        raise HTTPException(detail="this is duplicate name", status_code=404)
    crud.create_user(db, new_user)
    return model_schema.UserBaseSchema(**vars(user))


@router.post('/add_business')
def add_buisiness(business:model_schema.BusinessBase, db:Session=Depends(get_db)):
    if crud.get_business_name(db, business.business_name):
        raise HTTPException(detail="this is duplicate name", status_code=404)
    
    return crud.create_business(db, business)


@router.post('/upload_business_logo/{id}')
def upload_img_business(id:int, file:Union[UploadFile, None]=None, db:Session=Depends(get_db)):
    if file is None:
        return {"message":"dont upload image"}
    else:
        
        extension = file.filename.split('.')[1].lower()
        if not extension in ['jpg', 'png']:
            return {"message":"It is n't a image."}
        else:
            #read image
            image = Image.open(file.file)
            image = image.convert('RGB')
            buffer = BytesIO()
            image.save(buffer, format='JPEG')
            img_str = base64.b64encode(buffer.getvalue()).decode("utf8")

            crud.save_image_business(id, img_str, db)

            return {"message":"updated"}


@router.get("/log_business/{id}")
def show_img_logo(id:int, db:Session=Depends(get_db)):
    business = crud.get_business_id(db, id)
    if not business:
        return {"message":"It doesn't exist business."}
    else:
        image = business.logo
        if not image:
            return {"message":"It doesn't exist logo."}
        img_byte = base64.b64decode(image)
        img = BytesIO(img_byte)
        return StreamingResponse(img, media_type='image/JPEG')







