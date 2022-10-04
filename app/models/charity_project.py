from sqlalchemy import Column, String, Text

from .base import AbstractBase


class CharityProject(AbstractBase):
    """Модель для проектов пожертвований"""
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
