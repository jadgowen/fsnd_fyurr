"""empty message

Revision ID: f4c93072d2a5
Revises: e5ff0da82ffc
Create Date: 2020-05-11 12:44:43.582292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4c93072d2a5'
down_revision = 'e5ff0da82ffc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=1000), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=500), nullable=True))
    op.drop_column('Artist', 'num_upcoming_shows')
    op.drop_column('Venue', 'num_upcoming_shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('num_upcoming_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('num_upcoming_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
