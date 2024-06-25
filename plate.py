def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid():
        s = input("Plate: ")
        a = []
        n = []
        for i in s:
            if i.isalpha()== False:
                a.append(" ")
                n.append(i)
            elif i.isalpha()== True:
                a.append(i)
        if 2 <= len(s) <= 6:
            if s.isalpha()==True:
                print('OK')
            if a[len(s)-1]==a[len(s)-3] and a[len(s)-1]!=a[len(s)-2]:
                print('no OK')
            elif s.isalnum() and s[:2].isalpha() and n[0] != "0" and a[len(a)-1]==' ':
                print('OK')
            else:
                print('no OK')
        else:
            print('no ok')
        
        




is_valid()