"""add consumption table

Revision ID: 02808886c551
Revises: c8e1b9e23d89
Create Date: 2024-02-07 14:14:16.915043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02808886c551'
down_revision = 'c8e1b9e23d89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consumption',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('tko', sa.Float(precision=12), nullable=True),
    sa.Column('maintenance_common', sa.Float(precision=12), nullable=True),
    sa.Column('drainage_common', sa.Float(precision=12), nullable=True),
    sa.Column('cold_water_common', sa.Float(precision=12), nullable=True),
    sa.Column('hot_water_volume_common', sa.Float(precision=12), nullable=True),
    sa.Column('hot_water_energy_common', sa.Float(precision=12), nullable=True),
    sa.Column('electricity_common', sa.Float(precision=12), nullable=True),
    sa.Column('heating', sa.Float(precision=12), nullable=True),
    sa.Column('cold_water', sa.Float(precision=12), nullable=True),
    sa.Column('hot_water_volume', sa.Float(precision=12), nullable=True),
    sa.Column('hot_water_energy', sa.Float(precision=12), nullable=True),
    sa.Column('drainage', sa.Float(precision=12), nullable=True),
    sa.Column('gas', sa.Float(precision=12), nullable=True),
    sa.Column('renovation', sa.Float(precision=12), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('consumption', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_consumption_created_at'), ['created_at'], unique=False)

    with op.batch_alter_table('prices', schema=None) as batch_op:
        batch_op.alter_column('tko',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('maintenance_common',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('drainage_common',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('cold_water_common',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('hot_water_volume_common',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('hot_water_energy_common',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('electricity_common',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('heating',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('cold_water',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('hot_water_volume',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('hot_water_energy',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('drainage',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('gas',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('renovation',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prices', schema=None) as batch_op:
        batch_op.alter_column('renovation',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('gas',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('drainage',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('hot_water_energy',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('hot_water_volume',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('cold_water',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('heating',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('electricity_common',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('hot_water_energy_common',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('hot_water_volume_common',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('cold_water_common',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('drainage_common',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('maintenance_common',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('tko',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)

    with op.batch_alter_table('consumption', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_consumption_created_at'))

    op.drop_table('consumption')
    # ### end Alembic commands ###