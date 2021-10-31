import datetime
from typing import Optional
import ormar
from database import metadata, database


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=50)


class Video(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=30)
    description: str = ormar.String(max_length=300)
    file: str = ormar.String(max_length=1000)
    user: Optional[User] = ormar.ForeignKey(User)
