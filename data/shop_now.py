import sqlalchemy

from data.db_session import SqlAlchemyBase


class ShopNow(SqlAlchemyBase):
    __tablename__ = 'shop_now'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    shop_id = sqlalchemy.Column(sqlalchemy.Integer)
