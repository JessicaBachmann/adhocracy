import hashlib
import os
import logging
from datetime import datetime

from babel import Locale
from pylons import config
from pylons.i18n import _

from sqlalchemy import Table, Column, func, ForeignKey, or_
from sqlalchemy import Boolean, DateTime, Integer, Unicode, UnicodeText
from sqlalchemy.orm import eagerload_all

from adhocracy.model import meta
from adhocracy.model import instance_filter as ifilter
from adhocracy.model.core import JSONEncodedDict
from adhocracy.model.core import MutationDict
from adhocracy.model.instance import Instance
import logging
import meta
from sqlalchemy import MetaData




login_table = Table(
    'loginlog', meta.data,
    Column('id', Integer, primary_key=True),
    Column('access_time', DateTime, default=datetime.utcnow),
    Column('ip_address', Unicode(255), nullable=True),
    Column('user', UnicodeText()),
)

class Login(meta.Indexable):
    
    def __init__(self, access_time, ip_adress, user):
        self.access_time = datetime.utcnow()
        self.ip_address = ip_adress
        self.user = user
    
    @classmethod
    def store_login_attempt(cls, access_time, ip_adress, user ):
        l = Login(access_time, ip_adress, user)
        meta.Session.add(l)
        meta.Session.flush()
        meta.Session.commit()
        return l
        
        
    
    
