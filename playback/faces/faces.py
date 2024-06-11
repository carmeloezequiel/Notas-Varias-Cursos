def main():
    x = input()
    print(convert(x))



def convert(st):
    if '(' and ')' in st:
        x = st.replace(':(', '🙁')
        return x.replace(':)', '🙂')
    elif ')' in st:
      return  st.replace(':)', '🙂')
    elif '(' in st:
        return st.replace(':(', '🙁')
    

main()