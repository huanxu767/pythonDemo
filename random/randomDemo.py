import string,random

field = string.letters + string.digits

def getRandom():
    return "".join(random.sample(field,4))

getRandom()