t = 10

def main():
    for i in range(t):
        if i > t:
            raise ValueError('WTF?')
        elif i % 2 == 0:
            print('Foo')
        else:
            print('Bar')

main()

