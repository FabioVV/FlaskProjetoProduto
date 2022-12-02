"""better ranges

Revision ID: fdbe0a4bb208
Revises: de49ca40b37b
Create Date: 2022-12-02 10:36:04.679379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fdbe0a4bb208'
down_revision = 'de49ca40b37b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=25),
               type_=sa.String(length=70),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=25),
               type_=sa.String(length=70),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=25),
               type_=sa.String(length=300),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=25),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=70),
               type_=mysql.VARCHAR(length=25),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=70),
               type_=mysql.VARCHAR(length=25),
               existing_nullable=False)

    # ### end Alembic commands ###