class is_dig(Exception):
    def __init__(self,txt=' '):
        self.txt=txt

def list_complete()->list:
    l=[]
    while True:
        try:
            num=input('Enter the numeric values or enter "stop" to exit:\n')
            if num.isdigit():l.append(int(num))
            elif num=='stop': raise ValueError
            else: raise is_dig
        except is_dig:
            print('Wrong value, enter the numeric value')
        except ValueError:
                print(l)
                break


if __name__=="__main__":
    list_complete()