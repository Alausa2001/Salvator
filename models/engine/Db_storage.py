#!/usr/bin/python3
import models
from models.basemodel import BaseModel, Base
from models.login import UserLogin
from models.med_records import Records
from models.user_med_info import UserMedInfo
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

"""environment variables
    SAL_USER = salvator
    SAL_PWD = salvator_v1.0
    SAL_DB = salvator_db
    SAL_HOST = localhost
"""


class DbStorage:
    """handle operations like:
    1. database connection
    2. database query
    3. saving data into the database
    4. deleting data from the database
    """
    __engine = None
    __session = None

    def __init__(self):
        """creates a database connection"""
        user = getenv('SAL_USER')
        pwd = getenv('SAL_PWD')
        db = getenv('SAL_DB')
        host = getenv('SAL_HOST')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                 user, pwd, host, db))

    def reload(self):
        """creates db session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def new(self, obj):
        """adds and commit chab=nges to the database"""
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        """deletes an obj from the db"""
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """return and object with a id"""
        if cls is not None:
            obj = self.__session.query(cls).where(cls.id == id).first()
            if obj:
                return obj
            return None
        return None

    def close(self):
        """removes a session obj"""
        self.__session.remove()
    
    def all(self, cls=None):
        """gets all the instances of a class in the database
            cls is a string
        """
        all_obj = dict()
        if cls is not None:
            cls = eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = '.'.join([obj.__class__.__name__, obj.id])
                all_obj[key] = obj
        else:
            clas = [BaseModel, Records, UserMedInfo, UserLogin]
            for cls in clas:
                objs = self.session.query(cls).all()
                for obj in objs:
                    key = '.'.join([obj.__class__.__name__, obj.id])
                    all_obj[key] = obj
        return all_obj
