"""empty message

Revision ID: ae22290ec883
Revises: 9af0cfdf399b
Create Date: 2024-01-19 23:41:10.628216

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ae22290ec883'
down_revision = '9af0cfdf399b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ingredients', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('pizza_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('powers')
    op.drop_table('hero_powers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero_powers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('strength', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hero_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('power_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], name='hero_powers_power_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='hero_powers_pkey')
    )
    op.create_table('powers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='powers_pkey')
    )
    op.drop_table('restaurant_pizzas')
    op.drop_table('restaurants')
    op.drop_table('pizzas')
    # ### end Alembic commands ###
