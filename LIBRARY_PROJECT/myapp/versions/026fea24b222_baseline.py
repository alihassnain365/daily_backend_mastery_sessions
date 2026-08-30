"""baseline

Revision ID: 026fea24b222
Revises: 
Create Date: 2026-08-30 19:04:45.435263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '026fea24b222'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    


def downgrade() -> None:
    """Downgrade schema."""
    pass
