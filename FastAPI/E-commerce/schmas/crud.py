from models import model
from sqlalchemy.orm import Session


def get_business_name(db:Session, business_name:str):
    return db.query(model.Business).filter(model.Business.business_name==business_name).first()

def get_business_id(db:Session, id:str):
    return db.query(model.Business).filter(model.Business.id==id).first()

def create_business(db:Session, business):
    new_business = model.Business(**vars(business))
   
    db.add(new_business)
    db.flush()
    db.commit()
    db.refresh(new_business)
    return {"business":"saved"}
    

def create_user(db, new_user):
    db.add(new_user)
    db.flush()
    db.commit()
    db.refresh(new_user)
    return {"user":"saved"}


def get_user(db, username, email):
    user = db.query(model.User.username).filter(model.User.username==username).first()
    user2 = db.query(model.User).filter(model.User.email==email).first()
    return user, user2
        
def save_image_business(id, image, db):

    business = db.query(model.Business).filter(model.Business.id==id).first()
    if not business:
        return {"message":"it is n't exist."} 
    else:
        business.logo = image
        db.add(business)
        db.commit()
        db.refresh(business)

'''

        user = user.dict(exclude_unset=True)
        for key, value in user.items:
            setattr(db_user, key, value)
        '''