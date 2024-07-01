"""Add default value for received_at in EquipmentData

Revision ID: dd1c56e90f5a
Revises: 3e6b75bb05ac
Create Date: 2024-06-29 16:27:38.858567

"""
from typing import Sequence, Union

from sqlalchemy.sql import func

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'dd1c56e90f5a'
down_revision: Union[str, None] = '3e6b75bb05ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Alterar a tabela para definir um valor padrão para a coluna received_at
    op.alter_column('equipment_data', 'received_at', server_default=func.now())


def downgrade():
    # Remover o valor padrão para a coluna received_at
    op.alter_column('equipment_data', 'received_at', server_default=None)
