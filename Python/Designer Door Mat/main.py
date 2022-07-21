def design(n,m):
    # CREATE ABOVE "WELCOME"
    for i in range(n//2):
        for _ in range((m-((i*2)+1)*3)//2):
            print('-',end='')

        for _ in range((i*2)+1):
            print('.|.',end='')

        for _ in range((m-((i*2)+1)*3)//2):
            print('-',end='')

        print()
    
    # CREATE WELCOME
    for _ in range((m-6)//2):
        print('-',end='')

    print('WELCOME',end='')

    for _ in range((m-6)//2):
        print('-',end='')
    print()

    # CREATE BELOW "WELCOME"
    for i in range(n//2-1, -1, -1):
        for _ in range((m-((i*2)+1)*3)//2):
            print('-',end='')

        for _ in range((i*2)+1):
            print('.|.',end='')

        for _ in range((m-((i*2)+1)*3)//2):
            print('-',end='')

        print()
if __name__ == '__main__':
    n,m = input().split()
    design(int(n),int(m))