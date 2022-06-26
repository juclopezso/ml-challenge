"""my message

Revision ID: 20198b3ef89d
Revises: 
Create Date: 2022-06-25 20:21:39.228048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20198b3ef89d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###