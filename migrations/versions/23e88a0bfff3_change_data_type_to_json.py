"""change data type to JSON

Revision ID: 23e88a0bfff3
Revises: 1ffade2444f3
Create Date: 2014-08-20 15:00:50.964535

"""

# revision identifiers, used by Alembic.
revision = '23e88a0bfff3'
down_revision = '1ffade2444f3'

from alembic import op


def upgrade():
    op.execute('alter table titles alter column data type JSON using data::JSON')


def downgrade():
    op.execute('alter table titles alter column data type TEXT using data::TEXT')
