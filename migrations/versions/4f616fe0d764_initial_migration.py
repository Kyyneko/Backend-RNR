"""Initial migration

Revision ID: 4f616fe0d764
Revises: 
Create Date: 2024-10-24 22:26:10.371843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f616fe0d764'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shoe_category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=100), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('shoe_detail',
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('shoe_name', sa.String(length=100), nullable=False),
    sa.Column('shoe_price', sa.Float(), nullable=False),
    sa.Column('shoe_size', sa.String(length=10), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['shoe_category.category_id'], ),
    sa.PrimaryKeyConstraint('shoe_detail_id')
    )
    op.create_table('wallet',
    sa.Column('id_wallet', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('currency', sa.String(length=10), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id_wallet')
    )
    op.create_table('cart',
    sa.Column('id_cart', sa.Integer(), nullable=False),
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['shoe_detail_id'], ['shoe_detail.shoe_detail_id'], ),
    sa.PrimaryKeyConstraint('id_cart')
    )
    op.create_table('discount',
    sa.Column('id_discount', sa.Integer(), nullable=False),
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('discount_code', sa.String(length=50), nullable=False),
    sa.Column('discount_value', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('expiration_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['shoe_detail_id'], ['shoe_detail.shoe_detail_id'], ),
    sa.PrimaryKeyConstraint('id_discount'),
    sa.UniqueConstraint('discount_code')
    )
    op.create_table('gallery',
    sa.Column('gallery_id', sa.Integer(), nullable=False),
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['shoe_detail_id'], ['shoe_detail.shoe_detail_id'], ),
    sa.PrimaryKeyConstraint('gallery_id')
    )
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.Date(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('order_status', sa.String(length=50), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['shoe_detail_id'], ['shoe_detail.shoe_detail_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('user_interaction',
    sa.Column('interaction_id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('interaction_type', sa.Enum('view', 'wishlist', 'cart', 'order', name='interactiontype'), nullable=False),
    sa.Column('interaction_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['shoe_detail_id'], ['shoe_detail.shoe_detail_id'], ),
    sa.PrimaryKeyConstraint('interaction_id')
    )
    op.create_table('wishlist',
    sa.Column('id_wishlist', sa.Integer(), nullable=False),
    sa.Column('shoe_detail_id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['shoe_detail_id'], ['shoe_detail.shoe_detail_id'], ),
    sa.PrimaryKeyConstraint('id_wishlist')
    )
    op.create_table('payment',
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('payment_method', sa.String(length=50), nullable=False),
    sa.Column('payment_status', sa.String(length=50), nullable=False),
    sa.Column('payment_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('payment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('wishlist')
    op.drop_table('user_interaction')
    op.drop_table('order')
    op.drop_table('gallery')
    op.drop_table('discount')
    op.drop_table('cart')
    op.drop_table('wallet')
    op.drop_table('shoe_detail')
    op.drop_table('user')
    op.drop_table('shoe_category')
    # ### end Alembic commands ###
