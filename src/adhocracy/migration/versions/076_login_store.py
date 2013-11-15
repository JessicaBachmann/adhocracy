from datetime import datetime
from sqlalchemy import MetaData, Table, Boolean, Column
from sqlalchemy import Integer, DateTime, Unicode, UnicodeText

meta = MetaData()

login_table = Table('loginlog', meta,
    Column('id', Integer, primary_key=True),
    Column('access_time', DateTime, default=datetime.utcnow),
    Column('ip_address', Unicode(255), nullable=True),
    Column('user', UnicodeText()),
    Column('cookies', UnicodeText(), nullable=True),
    Column('user_agent', UnicodeText(), nullable=True),
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    login_table.create()

