"""Added product picture

Revision ID: 3d5ebac291fa
Revises: 2a6657ca1376
Create Date: 2022-12-02 13:46:51.196641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5ebac291fa'
down_revision = '2a6657ca1376'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('produtc_pic', sa.String(length=300), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('produtc_pic')

    # ### end Alembic commands ###
