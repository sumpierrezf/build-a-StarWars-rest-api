"""empty message

Revision ID: 56da29d4c9e8
Revises: ba8a75936a1f
Create Date: 2023-01-26 20:00:59.175160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56da29d4c9e8'
down_revision = 'ba8a75936a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favourite')
    # ### end Alembic commands ###