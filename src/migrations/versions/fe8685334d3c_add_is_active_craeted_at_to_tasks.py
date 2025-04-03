"""add is_active, craeted_at to tasks

Revision ID: fe8685334d3c
Revises: 8a79d2906a93
Create Date: 2025-04-03 01:23:26.895146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe8685334d3c'
down_revision: Union[str, None] = '8a79d2906a93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('tasks', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'created_at')
    op.drop_column('tasks', 'is_active')
    # ### end Alembic commands ###
