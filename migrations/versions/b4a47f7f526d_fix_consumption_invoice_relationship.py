"""fix consumption - invoice relationship

Revision ID: b4a47f7f526d
Revises: 21538d992127
Create Date: 2024-02-08 10:33:04.194404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4a47f7f526d'
down_revision = '21538d992127'
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
