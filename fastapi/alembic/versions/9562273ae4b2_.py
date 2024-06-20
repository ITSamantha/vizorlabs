"""empty message

Revision ID: 9562273ae4b2
Revises: 9cc3388424f0
Create Date: 2024-06-20 13:11:43.836626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9562273ae4b2'
down_revision: Union[str, None] = '9cc3388424f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'business_trips', 'employees', ['employee_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'employees', 'employee_positions', ['position_id'], ['id'], ondelete='SET NULL', use_alter=True)
    op.create_foreign_key('fk_employee_unit_id', 'employees', 'units', ['unit_id'], ['id'], ondelete='SET NULL', use_alter=True)
    op.create_foreign_key('fk_unit_director_id', 'units', 'employees', ['director_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'vacations', 'employees', ['employee_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'vacations', 'vacation_reasons', ['vacation_reason_id'], ['id'], ondelete='SET NULL', use_alter=True)
    op.create_foreign_key(None, 'vacations', 'vacation_types', ['vacation_type_id'], ['id'], ondelete='SET NULL', use_alter=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vacations', type_='foreignkey')
    op.drop_constraint(None, 'vacations', type_='foreignkey')
    op.drop_constraint(None, 'vacations', type_='foreignkey')
    op.drop_constraint('fk_unit_director_id', 'units', type_='foreignkey')
    op.drop_constraint('fk_employee_unit_id', 'employees', type_='foreignkey')
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.drop_constraint(None, 'business_trips', type_='foreignkey')
    # ### end Alembic commands ###