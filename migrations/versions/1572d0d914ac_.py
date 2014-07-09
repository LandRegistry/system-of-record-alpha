"""empty message

Revision ID: 1572d0d914ac
Revises: None
Create Date: 2014-07-08 16:57:37.147754

"""

# revision identifiers, used by Alembic.
revision = '1572d0d914ac'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_number', sa.String(length=64), nullable=True),
    sa.Column('data', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('titles')
    ### end Alembic commands ###