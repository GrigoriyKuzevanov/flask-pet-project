"""add electricity field to price model

Revision ID: 834a99cdd837
Revises: e2737c824728
Create Date: 2024-02-09 17:16:33.369904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '834a99cdd837'
down_revision = 'e2737c824728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('consumption', schema=None) as batch_op:
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
        batch_op.alter_column('electricity',
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

    with op.batch_alter_table('invoices', schema=None) as batch_op:
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
        batch_op.alter_column('electricity',
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
        batch_op.alter_column('common_total',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('variable_total',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('total',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)

    with op.batch_alter_table('prices', schema=None) as batch_op:
        batch_op.add_column(sa.Column('electricity', sa.Float(precision=12), nullable=True))
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
        batch_op.drop_column('electricity')

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.alter_column('total',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('variable_total',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('common_total',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('renovation',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('gas',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('electricity',
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
        batch_op.alter_column('renovation',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('gas',
               existing_type=sa.Float(precision=12),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('electricity',
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

    # ### end Alembic commands ###