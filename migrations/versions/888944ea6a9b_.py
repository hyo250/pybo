"""empty message

Revision ID: 888944ea6a9b
Revises: 15f5db03f400
Create Date: 2021-05-04 16:51:38.759580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '888944ea6a9b'
down_revision = '15f5db03f400'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', sa.String(length=40), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'address')
    # ### end Alembic commands ###
