class IceCreamFlavor:
    def __init__(self, flavor_name, is_savory):
        self.flavor_name = flavor_name
        self.is_savory = is_savory

    def __str__(self):
        return "{} and is {}".format(
            self.flavor_name,
            "savory" if self.is_savory else "not savory"
    )

ice_cream_flavors = {
    "a": IceCreamFlavor("Strawberry", False),
    "b": IceCreamFlavor("Onion", True)
}

for key, value in ice_cream_flavors.items():
    if value.is_savory is False:
        print("{}: {}".format(key, value))

---------------------------------------

def __str__(self):
    return "{} and is {}".format(
        self.good,
        "good" if self.good else "bad"

for key, value in characters.items():
if value.good is False:
    print("{}: {}".format(key, value))
