############
# Part 1   #
############


from ctypes.wintypes import PINT


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    # def __repr__(self):
    #     return f"<MelonType code={self.code} pairings={self.pairings}>"


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        
        


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "Green", False, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw",2013,"yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types
    

# for melon in make_melon_types():
#     print(melon.__dict__)

# print(make_melon_types())

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    #loop all_melon_types, musk then cas.. 
    #for melon_type in melon_types:
    
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")
    
    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # create an empty dic
    melon_type_code = {} 

    # loop through diff melon type
    for melon in melon_types:
    # for each type, add its code as the key(string) dic[melon.code] = melon.name
        # print(melon.code, type(melon))
        melon_type_code[melon.code] = melon
    # return the empty dic
    return melon_type_code
    
# {yw: ["yw",2013,"yellow", True, True, "Yellow Watermelon"]}

# print(make_melon_type_lookup(make_melon_types()))



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # def a __init__(self, type, shape_rating, color_rating, field, harvested_by):
    def __init__(self, type, shape_rating, color_rating, field, harvested_by):
    #   set attributes accordingly, e.g. self.type = type
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by
    
    
    # def is_sellable():
    def is_sellable(self):
        
    #   if self.shape_rating >5 and self.color_rating >5 and field != 3:
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
    #       return True
            return True
    #   else"
    #       return False
        else:
            return False
    


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_type_code = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_type_code["yw"],8,7,2,"Sheila")

    melon_2 = Melon(melon_type_code["yw"],3,4,2,"Sheila")

    melon_3 = Melon(melon_type_code["yw"],9,8,3,"Sheila")

    melon_4 = Melon(melon_type_code["cas"],10,6,35,"Sheila")

    melon_5 = Melon(melon_type_code["cren"],8,9,35,"Michael")
  
    melon_6 = Melon(melon_type_code["cren"], 8, 2, 35, "Michael")

    melon_7 = Melon(melon_type_code["cren"], 2, 3, 4, "Michael")

    melon_8 = Melon(melon_type_code["musk"], 6, 7, 4, "Michael")
    
    melon_9 = Melon(melon_type_code["yw"], 7, 10, 3, "Michael")
    
    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9,
    ]
    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # loop through the list to capture each melon from 1-9
    #   for each_melon in melones:
    for melon in melons:
    #     if each_melon.is_sellable is True:
        if melon.is_sellable() is True:
            print(f"Harvested by {melon.harvested_by} from Field {melon.field} (CAN BE SOLD)")

        else:
            print(f"Harvested by {melon.harvested_by} from Field {melon.field} (NOT SELLABLE)")



print(get_sellability_report(make_melons(make_melon_types())))



#for melon in make_melon_types():
    #print(melon.__dict__)

# def __repr__(self):
#    return f”< MelonType, code = {self.code}”
