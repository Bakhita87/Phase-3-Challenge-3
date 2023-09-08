"""Initial migration

Revision ID: cf27da1d6454
Revises: 
Create Date: 2023-09-08 13:26:25.547208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf27da1d6454'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Customers",
                   sa.Column("id",sa.Integer),
                   sa.Column("first_name",sa.String),
                   sa.Column("last_name",sa.String),
                   sa.PrimaryKeyConstraint("id")
                    
                    )
    op.create_table("Restaurants",
                   sa.Column("id",sa.Integer),
                   sa.Column("name",sa.String),
                   sa.Column("price",sa.Integer),
                   sa.PrimaryKeyConstraint("id")
                    
                    )
    op.create_table("Reviews",
                   sa.Column("id",sa.Integer),
                   sa.Column("rating",sa.Integer),
                   sa.Column("restaurant_id",sa.Integer(),sa.ForeignKey("restaurants.id")),
                   sa.Column("customer_id",sa.Integer(),sa.ForeignKey("customers.id")),
                   sa.PrimaryKeyConstraint("id")
                    
                    )
    


def downgrade() -> None:
    op.drop_table("Customers")
    op.drop_table("Restaurants")
    op.drop_table("Reviews")
