"""

Revision ID: 1df9a79eb4b7
Revises: 1ffade2444f3
Create Date: 2014-09-11 11:56:38.611188

"""


# revision identifiers, used by Alembic.
from sqlalchemy import Integer, String, Sequence, ForeignKey, Column
from sqlalchemy.sql.ddl import CreateSequence, DropSequence

revision = '1df9a79eb4b7'
down_revision = '1ffade2444f3'

from alembic import op


def upgrade():
    op.execute(CreateSequence(Sequence('tag_id_seq')))

    op.create_table(
        'tag',
        Column('id', Integer(), Sequence('tag_id_seq'), primary_key=True),
        Column('name', String(), nullable=False),
        Column('value', String(), nullable=False),
        Column('record_id', Integer(), ForeignKey('blockchain.id'), nullable=False),
        Column('record_seq', Integer(), nullable=False)
    )

    op.create_unique_constraint('uq_tag_name_and_value', 'tag', ['name', 'value', 'record_id'])


def downgrade():
    op.dropTable('tag')
    op.execute(DropSequence('tag_id_seq'))
    op.drop_constraint('uq_tag_name_and_value')
