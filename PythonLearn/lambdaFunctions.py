#Lambda functions (also called anonymous)
#classic function build
def add(x, y):
    return x + y
print(add(10, 5))
#now the Lambda version
add = lambda x, y: x + y
print(add(10, 5))
