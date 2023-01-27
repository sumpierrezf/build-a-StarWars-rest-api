"""empty message

Revision ID: 0e64f8959cae
Revises: 0b2215bc6d55
Create Date: 2023-01-26 14:53:14.985569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e64f8959cae'
down_revision = '0b2215bc6d55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('single__user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('character')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('character_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('eye_color', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('hair_color', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('skin_color', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='character_pkey')
    )
    op.drop_table('single__user')
    # ### end Alembic commands ###