from sqlalchemy import Column, Text, Integer, ForeignKey

from .base import AbstractBase


class Donation(AbstractBase):
    """Модель для пожертвований"""
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
