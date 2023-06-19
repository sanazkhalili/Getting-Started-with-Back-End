"""create database

Revision ID: fda076eb06e6
Revises: 
Create Date: 2023-06-17 16:11:48.746063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda076eb06e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('join_data', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business_name', sa.String(length=20), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('region', sa.String(length=100), nullable=False),
    sa.Column('business_description', sa.Text(), nullable=True),
    sa.Column('logo', sa.String(length=200), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('business_name')
    )
    op.create_index(op.f('ix_business_id'), 'business', ['id'], unique=False)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=True),
    sa.Column('original_price', sa.DECIMAL(), nullable=True),
    sa.Column('percentag_discount', sa.Integer(), nullable=True),
    sa.Column('offer_expiration_data', sa.DateTime(timezone=True), nullable=True),
    sa.Column('product_image', sa.String(length=200), nullable=False),
    sa.Column('business', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business'], ['business.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_category'), 'product', ['category'], unique=False)
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_index(op.f('ix_product_category'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_business_id'), table_name='business')
    op.drop_table('business')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
