"""empty message

Revision ID: 0b9e3224530c
Revises: 
Create Date: 2020-05-11 09:35:53.815386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b9e3224530c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upcoming_or_past', sa.Boolean(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Artist', sa.Column('num_upcoming_shows', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.PickleType(), nullable=True))
    op.add_column('Venue', sa.Column('num_upcoming_shows', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=1000), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'num_upcoming_shows')
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'num_upcoming_shows')
    op.drop_table('Shows')
    # ### end Alembic commands ###