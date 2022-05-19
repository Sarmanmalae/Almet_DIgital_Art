import sqlalchemy

from data.db_session import SqlAlchemyBase


class Shops(SqlAlchemyBase):
    __tablename__ = 'shops'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    tg_name = sqlalchemy.Column(sqlalchemy.String)
    specific_gps = sqlalchemy.Column(sqlalchemy.String)
    which_map = sqlalchemy.Column(sqlalchemy.Integer)
    color = sqlalchemy.Column(sqlalchemy.String)
