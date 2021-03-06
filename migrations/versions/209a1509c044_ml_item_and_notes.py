"""ML item and notes

Revision ID: 209a1509c044
Revises: 
Create Date: 2022-06-26 21:17:42.927429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '209a1509c044'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('site', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('nickname', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_item_nickname'), 'item', ['nickname'], unique=True)
    op.create_table('note',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('starred', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_index(op.f('ix_item_nickname'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###
