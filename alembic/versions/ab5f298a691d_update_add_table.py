"""update add table

Revision ID: ab5f298a691d
Revises: 0834abd74b8a
Create Date: 2023-11-24 19:42:54.972498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab5f298a691d'
down_revision: Union[str, None] = '0834abd74b8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.String(length=100), autoincrement=False, nullable=False),
    sa.Column('id_volunteer', sa.String(length=100), nullable=False),
    sa.Column('question1', sa.String(length=100), nullable=False),
    sa.Column('question2', sa.String(length=100), nullable=False),
    sa.Column('question3', sa.String(length=100), nullable=False),
    sa.Column('question4', sa.String(length=100), nullable=False),
    sa.Column('question5', sa.String(length=100), nullable=False),
    sa.Column('question6', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voter',
    sa.Column('id', sa.String(length=100), autoincrement=False, nullable=False),
    sa.Column('nkk', sa.String(length=100), nullable=True),
    sa.Column('nik', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('birth_date', sa.String(length=100), nullable=True),
    sa.Column('place_of_birth', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=True),
    sa.Column('phone_number', sa.String(length=100), nullable=True),
    sa.Column('province', sa.String(length=100), nullable=True),
    sa.Column('regency', sa.String(length=100), nullable=True),
    sa.Column('district', sa.String(length=100), nullable=True),
    sa.Column('village', sa.String(length=100), nullable=True),
    sa.Column('rt', sa.String(length=100), nullable=True),
    sa.Column('rw', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('ktp', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.String(length=100), autoincrement=False, nullable=False),
    sa.Column('id_voter', sa.String(length=100), nullable=False),
    sa.Column('q1', sa.Boolean(), nullable=True),
    sa.Column('q2', sa.Boolean(), nullable=True),
    sa.Column('q3', sa.Boolean(), nullable=True),
    sa.Column('q4', sa.Boolean(), nullable=True),
    sa.Column('q5', sa.Boolean(), nullable=True),
    sa.Column('q6', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_voter'], ['voter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    op.drop_table('voter')
    op.drop_table('question')
    # ### end Alembic commands ###
