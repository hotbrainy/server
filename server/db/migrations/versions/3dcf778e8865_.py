"""empty message

Revision ID: 3dcf778e8865
Revises: 8fc2bbbf48b0
Create Date: 2022-11-21 01:37:15.681665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dcf778e8865'
down_revision = '8fc2bbbf48b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('external_id', sa.String(length=32), nullable=False))
        batch_op.add_column(sa.Column('token_id', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('_password', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('is_confirmed', sa.Boolean(), nullable=False))
        batch_op.alter_column('registered_on',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['token_id'])
        batch_op.create_unique_constraint(None, ['external_id'])
        batch_op.drop_column('admin')
        batch_op.drop_column('password')
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.BOOLEAN(), nullable=False))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('admin', sa.BOOLEAN(), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('registered_on',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.drop_column('is_confirmed')
        batch_op.drop_column('is_admin')
        batch_op.drop_column('_password')
        batch_op.drop_column('token_id')
        batch_op.drop_column('external_id')

    # ### end Alembic commands ###
