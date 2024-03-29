"""add category

Revision ID: 9d851efd9248
Revises: 607adc45deca
Create Date: 2022-06-02 01:08:35.876043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d851efd9248'
down_revision = '607adc45deca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('category', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'category')
    # ### end Alembic commands ###
