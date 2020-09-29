class BasicPlan:
    stream = True
    download = True
    devices = 1
    SD = True
    HD = False
    UHD = False
    harga = '100.000 IDR'


class StandardPlan(BasicPlan):
    devices = 2
    HD = True
    harga = '400.000 IDR'


class PremiumPlan(StandardPlan):
    devices = 4
    UHD = True
    harga = '600.000 IDR'


print(BasicPlan.SD)
print(PremiumPlan.SD)
print(BasicPlan.UHD)
print(BasicPlan.harga)
print(PremiumPlan.devices)
