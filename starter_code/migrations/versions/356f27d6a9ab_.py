"""empty message

Revision ID: 356f27d6a9ab
Revises: f4c93072d2a5
Create Date: 2020-05-11 15:58:47.569604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356f27d6a9ab'
down_revision = 'f4c93072d2a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###