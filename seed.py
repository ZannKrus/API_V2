from sqlalchemy.orm import Session
from database import engine
import models as m

m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    p1=m.Product(name='Молоко')
    session.add(p1)

    session.commit()
