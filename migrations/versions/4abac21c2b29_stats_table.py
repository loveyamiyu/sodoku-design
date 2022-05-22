"""stats table

Revision ID: 4abac21c2b29
Revises: fee8fd4161d9
Create Date: 2022-05-22 18:05:56.306606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4abac21c2b29'
down_revision = 'fee8fd4161d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puzzle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('puzzle', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('stats', sa.Column('puzzle', sa.JSON(), nullable=True))
    op.alter_column('stats', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index('ix_stats_finishTime', table_name='stats')
    op.drop_index('ix_stats_startTime', table_name='stats')
    op.drop_column('stats', 'finishTime')
    op.drop_column('stats', 'startTime')
    op.drop_column('stats', 'difficulty')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('difficulty', sa.VARCHAR(length=140), nullable=True))
    op.add_column('stats', sa.Column('startTime', sa.DATETIME(), nullable=True))
    op.add_column('stats', sa.Column('finishTime', sa.DATETIME(), nullable=True))
    op.create_index('ix_stats_startTime', 'stats', ['startTime'], unique=False)
    op.create_index('ix_stats_finishTime', 'stats', ['finishTime'], unique=False)
    op.alter_column('stats', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('stats', 'puzzle')
    op.drop_table('puzzle')
    # ### end Alembic commands ###