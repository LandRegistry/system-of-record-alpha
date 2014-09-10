"""empty message

Revision ID: 1ffade2444f3
Revises: None
Create Date: 2014-07-18 12:11:21.405386

"""

from sqlalchemy import Column, Integer, String, TEXT, Sequence, Index
from sqlalchemy.sql.ddl import CreateSequence, DropSequence

revision = '1ffade2444f3'
down_revision = None

from alembic import op


def upgrade():
    op.execute(CreateSequence(Sequence('title_id_seq')))
    op.execute(CreateSequence(Sequence('blockchain_index_seq')))

    op.create_table(
        'title',
        Column('id', Integer(), Sequence('title_id_seq'), primary_key=True),
        Column('title_number', String(length=64), nullable=False),
        Column('creation_timestamp', Integer(), nullable=False),
        Column('data', TEXT(), nullable=False),
        Column('blockchain_index',
               Integer(), Sequence('blockchain_index_seq'), nullable=False, unique=True),
        Index('idx_title', 'id', 'title_number', 'blockchain_index', 'creation_timestamp', unique=True)
    )


def downgrade():
    op.drop_table('titles')
    op.execute(DropSequence('title_id_seq'))
    op.execute(DropSequence('blockchain_index_seq'))

