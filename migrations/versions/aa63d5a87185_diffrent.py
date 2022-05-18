"""diffrent

Revision ID: aa63d5a87185
Revises: 7820ac5bc7e4
Create Date: 2022-05-18 18:43:11.532627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa63d5a87185'
down_revision = '7820ac5bc7e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('details', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'details')
    # ### end Alembic commands ###
