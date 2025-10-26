with open('input.txt', 'a+') as f:
    f.write('\nthe phrase is taken from Jane Austen book "Sense and Sensibility"')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)