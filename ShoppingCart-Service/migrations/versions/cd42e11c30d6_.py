"""empty message

Revision ID: cd42e11c30d6
Revises: 375444b3b32c
Create Date: 2022-11-22 11:25:06.979318

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cd42e11c30d6'
down_revision = '375444b3b32c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shoppingcart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))
        batch_op.drop_column('total')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shoppingcart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total', mysql.FLOAT(), nullable=False))
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###