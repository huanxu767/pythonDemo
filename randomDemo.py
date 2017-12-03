import string, random

field = string.letters + string.digits

def getRandom():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

if __name__ == '__main__':
    print concatenate(5)