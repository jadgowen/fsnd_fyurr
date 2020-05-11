"""empty message

Revision ID: e5ff0da82ffc
Revises: 0b9e3224530c
Create Date: 2020-05-11 12:19:50.186628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5ff0da82ffc'
down_revision = '0b9e3224530c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('show_time', sa.DateTime(), nullable=False))
    op.drop_column('Shows', 'upcoming_or_past')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('upcoming_or_past', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('Shows', 'show_time')
    # ### end Alembic commands ###
