import sys

def main():
    try:
        if len(sys.argv) == 2:
            count =  count_lines(sys.argv[1])
            print(count)
        else:
           sys.exit('Muchos Argumentos') 
    except IndexError:
        sys.exit('Pocos argumentos')
        
    
    
    
def count_lines(file):
    try:
        if '.py' in file:
            with open(f'{file}', 'r') as file:
                count = 0
                for row in file:
                    if len(row.lstrip()) > 0 and row[0] != '#':
                        count += 1
                    else:
                        pass
                return count
        else:
            sys.exit('No es archivo python')
            
    except FileNotFoundError:
        sys.exit('No existe este archivo python')


main()