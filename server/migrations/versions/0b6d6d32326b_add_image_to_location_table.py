"""add image to location table

Revision ID: 0b6d6d32326b
Revises: d55b804ca2ee
Create Date: 2024-07-11 13:39:21.164441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b6d6d32326b'
down_revision = 'd55b804ca2ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
