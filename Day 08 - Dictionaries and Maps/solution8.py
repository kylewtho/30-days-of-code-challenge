# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input(''))
contacts = dict()
for i in range(n):
    name, number = input('').split()
    contacts[name] = number
while True:
    try:
        name_check = input('')
        if name_check in contacts:
            print(f'{name_check}={contacts[name_check]}')
        else:
            print('Not found')
    except:
        break
