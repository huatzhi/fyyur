"""empty message

Revision ID: 1fa6d0be4b2d
Revises: 6a8c300b3c8e
Create Date: 2020-01-15 07:01:10.686953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fa6d0be4b2d'
down_revision = '6a8c300b3c8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artist_genres',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )
    op.create_table('venue_genres',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'genre_id')
    )
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_table('venue_genres')
    op.drop_table('artist_genres')
    op.drop_table('Genre')
    # ### end Alembic commands ###