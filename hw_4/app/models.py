from pydantic import BaseModel


class Order(BaseModel):
    order_type: str
    item_name: str
    item_price: int
