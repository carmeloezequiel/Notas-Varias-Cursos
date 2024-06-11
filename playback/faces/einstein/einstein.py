def main():
    m = int(input('m: '))
    energy(m)
    
def energy(mass):
    E = mass * pow(300000000, 2 )
    print(f'E: {E}')
    
main()