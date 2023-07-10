from materio.models.base import Maxsulot
from materio.models.base import Storage, Storage_order


def maxsulot_format(data: Maxsulot):
    return {
        "id": data.id,
        "product_name": data.product_name,
        "size": data.size,
        "color": data.color,
        "joyi": data.joyi,
        "product_price": data.product_price,
        "prodect_price_type": data.product_price_type,
        "entry_price": data.entry_price,
        "entry_price_type": data.entry_price_type
    }
