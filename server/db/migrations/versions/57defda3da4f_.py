"""empty message

Revision ID: 57defda3da4f
Revises: 0874fd79a6ea
Create Date: 2022-11-14 19:40:58.705595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57defda3da4f'
down_revision = '0874fd79a6ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token_id', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('phone_number', sa.String(length=100), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.Column('confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('token_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
