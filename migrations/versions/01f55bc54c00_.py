"""empty message

Revision ID: 01f55bc54c00
Revises: 08305989c396
Create Date: 2023-03-07 11:46:07.745110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01f55bc54c00'
down_revision = '08305989c396'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessons',
    sa.Column('lid', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('sections_num', sa.Integer(), nullable=True),
    sa.Column('sections_intro', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('lid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lessons')
    # ### end Alembic commands ###
