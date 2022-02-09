from product import Product
from store import Store

real_beauty = Store("Real Beauty")

lipstick1 = Product("Raspberry Rue", 6, "lips")
lipstick2 = Product("Cotton Candy Pink", 7, "lips")

skin1 = Product("Cetaphil Skin Cleaner", 12, "skin care")
skin2 = Product("CeraVe Skin Cleaner", 12, "skin care")

palette1 = Product("Tapatillo Shadows", 30, "palettes")
palette2 = Product("Morphe Eyelid Dyes", 30, "palettes")

real_beauty.add_product(lipstick1).add_product(lipstick2).add_product(skin1).add_product(skin2).add_product(palette1).add_product(palette2)

for i in range(len(real_beauty.products)):
    real_beauty.products[i].print_info()
print()

real_beauty.sell_product(1)
print()

for i in range(len(real_beauty.products)):
    real_beauty.products[i].print_info()
print()

real_beauty.inflation(0.25)
for i in range(len(real_beauty.products)):
    real_beauty.products[i].print_info()
print()

real_beauty.set_clearance("skin care", .4)
for i in range(len(real_beauty.products)):
    real_beauty.products[i].print_info()
print()