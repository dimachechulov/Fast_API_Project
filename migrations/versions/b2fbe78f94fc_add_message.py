"""Add message

Revision ID: b2fbe78f94fc
Revises: 2ed39fcdd5df
Create Date: 2024-05-03 19:51:45.381770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2fbe78f94fc'
down_revision: Union[str, None] = '2ed39fcdd5df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###