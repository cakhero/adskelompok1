"""init

Revision ID: 9588b23d58f6
Revises: 
Create Date: 2023-05-18 17:13:57.304808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9588b23d58f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('UserID', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('report_bug', sa.Text, nullable=True)
    )
    op.create_table(
        'pemberi_rekomendasi',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nama_warung', sa.String(), nullable=True),
        sa.Column('lokasi_warung', sa.String(), nullable=True),
        sa.Column('jam_buka_warung', sa.String(), nullable=True),
        sa.Column('kontak_warung', sa.Integer(), nullable=True),
        sa.Column('nama_makanan', sa.String(), nullable=True),
        sa.Column('harga_makanan', sa.Integer(), nullable=True),
        sa.Column('nama_minuman', sa.String(), nullable=True),
        sa.Column('harga_minuman', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'mahasiswa',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nominal_dana', sa.Integer(), nullable=True),
        sa.Column('durasi_hari', sa.Integer(), nullable=True),
        sa.Column('nilai_warung', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    

def downgrade() -> None:
    op.drop_table('user')
    op.drop_table('pemberi_rekomendasi')
    op.drop_table('mahasiswa')
