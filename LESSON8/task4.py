class is_dig(Exception):
    def __init__(self,txt=' '):
        self.txt=txt

class OfficeEquip:
    def __init__(self,inventory_name,brand,year,country_manufacture):
        self.inventory_name=inventory_name
        self.brand=brand
        self.year=year
        self.country_manufacture=country_manufacture


class Printer(OfficeEquip):
    def __init__(self,inventory_name,brand,year,country_manufacture,p_per_min,ink_consum):
        self.p_per_min=p_per_min
        self.ink_consum=ink_consum
        super().__init__(inventory_name,brand,year,country_manufacture)

class Scanner(OfficeEquip):
    def __init__(self,inventory_name,brand,year,country_manufacture,max_resolution):
        super().__init__(inventory_name,brand,year,country_manufacture)
        self.max_resolution=max_resolution
class Xerox(OfficeEquip):
    def __init__(self,inventory_name,brand,year,country_manufacture,tray_size):
        super().__init__(inventory_name, brand, year, country_manufacture)
        self.tray_size=tray_size

# printer1=Printer('id123','Samsung',2010,'China',198,10)
# print(printer1.p_per_min)


class Warehouse:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.list_of_items={}

    def add_to_warehouse(self,count,cls_equip,**kwargs):
        try:
            if count.isdigit():return {cls_equip(**kwargs):count for _ in range(count)}
            else:raise is_dig
        except is_dig:
            print("The first argument should be numeric")


       #return self.list_of_items.update({cls_equip(kwargs):count for _ in count})
       #print(cls_equip('id123','Samsung',2010,'China',198,10))
       #return cls_equip(*kwargs)
    # def give_to_depart(self,count,cl_equip):
    #     pass
warehouse1=Warehouse('LTD Alex Warehouse','Los Angeles')
lst=warehouse1.add_to_warehouse(10,Printer,inventory_name='id43',brand='Samsung',year=2010,country_manufacture='China',p_per_min=103,ink_consum=10)
print(lst)