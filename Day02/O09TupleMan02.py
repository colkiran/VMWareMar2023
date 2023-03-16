
from collections import namedtuple

nmdTpl = namedtuple("Products", "prodid pname price")
prod = nmdTpl(prodid=101, pname="Pepsi", price=25)
print(f"prod :{prod}")

print("-" * 40)
print(f"Product ID   :{prod.prodid}")
print(f"Product Name :{prod.pname}")
print(f"Price        :{prod.price}")

prod.pname = "Thumbs up"
