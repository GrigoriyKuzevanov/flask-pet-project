"""empty message

Revision ID: 3a30afba5362
Revises: 1d8809778444
Create Date: 2024-02-07 15:25:03.438081

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3a30afba5362'
down_revision = '1d8809778444'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoices',
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
    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_invoices_created_at'), ['created_at'], unique=False)

    with op.batch_alter_table('invoice_model', schema=None) as batch_op:
        batch_op.drop_index('ix_invoice_model_created_at')

    op.drop_table('invoice_model')
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

    op.create_table('invoice_model',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('tko', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('maintenance_common', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('drainage_common', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('cold_water_common', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('hot_water_volume_common', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('hot_water_energy_common', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('electricity_common', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('heating', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('cold_water', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('hot_water_volume', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('hot_water_energy', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('drainage', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('gas', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('renovation', sa.REAL(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='invoice_model_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='invoice_model_pkey')
    )
    with op.batch_alter_table('invoice_model', schema=None) as batch_op:
        batch_op.create_index('ix_invoice_model_created_at', ['created_at'], unique=False)

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_invoices_created_at'))

    op.drop_table('invoices')
    # ### end Alembic commands ###
