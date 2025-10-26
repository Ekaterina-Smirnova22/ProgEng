lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nLine numberSSs ' + line)
    print('Done!')