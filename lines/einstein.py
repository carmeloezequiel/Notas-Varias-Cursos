# Este es un comentario 

def main():
    m = int(input('m: '))
    energy(m)
    
def energy(mass):
    E = mass * pow(300000000, 2 )
    print(f'E: {E}')
    
if __name__ == '__main__':
    main()