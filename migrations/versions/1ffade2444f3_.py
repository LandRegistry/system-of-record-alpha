"""empty message

Revision ID: 1ffade2444f3
Revises: None
Create Date: 2014-07-18 12:11:21.405386

"""

# revision identifiers, used by Alembic.
revision = '1ffade2444f3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('titles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title_number', sa.String(length=64), nullable=True),
                    sa.Column('data', sa.TEXT(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('titles')
