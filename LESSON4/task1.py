import sys
print(sys.argv)
_,hours,rate,award=sys.argv
try:
    hours=int(hours)
    rate=int(rate)
    award=int(award)
except:
    print("enter numeric values")

def calc_salary(hours:float,rate:float,award:float)->float:
     return (hours*rate)+award

if __name__=="__main__":
    print(calc_salary(hours,rate,award))