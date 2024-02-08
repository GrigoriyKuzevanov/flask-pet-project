"""add relations invoice - counsumption

Revision ID: 21538d992127
Revises: 3a30afba5362
Create Date: 2024-02-08 10:26:05.803590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21538d992127'
down_revision = '3a30afba5362'
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
        batch_op.alter_column('gas',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)
        batch_op.alter_column('renovation',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=12),
               existing_nullable=True)

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.add_column(sa.Column('consumption_id', sa.Integer(), nullable=True))
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
        batch_op.create_foreign_key(None, 'consumption', ['consumption_id'], ['id'])

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

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
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
        batch_op.drop_column('consumption_id')

    with op.batch_alter_table('consumption', schema=None) as batch_op:
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

    # ### end Alembic commands ###