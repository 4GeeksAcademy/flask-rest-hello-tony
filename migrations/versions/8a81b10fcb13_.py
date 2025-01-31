"""empty message

Revision ID: 8a81b10fcb13
Revises: a5cffa318ac2
Create Date: 2024-01-23 23:29:41.972079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a81b10fcb13'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('race', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('last_name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('subscription_date', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.create_table('favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.Column('id_planeta', sa.Integer(), nullable=True),
    sa.Column('id_personaje', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_personaje'], ['personaje.id'], ),
    sa.ForeignKeyConstraint(['id_planeta'], ['planeta.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('favorito')
    op.drop_table('usuario')
    op.drop_table('planeta')
    op.drop_table('personaje')
    # ### end Alembic commands ###
