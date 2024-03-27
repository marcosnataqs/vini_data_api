from sqlalchemy.orm import DeclarativeBase

from vini_data_api.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
