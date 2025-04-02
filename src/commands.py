import os

from alembic import command
from alembic.config import Config


def run_migrations():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), '..', 'alembic.ini'))
    command.upgrade(alembic_cfg, "head")