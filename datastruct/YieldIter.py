## eg1:
def countIter(n):
    while n>0:
        yield n
        n -= 1
    print("next end")

for i in countIter(5):
    print(i)

# "yield" key mean return a next(), when a iterator was used, next() would be used.
# One benefit of "yield" is void to store data with a list, save memory.
# 05-04: when you execute countIter() return a iterator. So, 'for i in countIter(5)' means countIter.next...

## eg2:
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

## eg3:
for i in countIter(5):
    if( i<3 ):
        break;
    print(i)
# result: 5,4,3