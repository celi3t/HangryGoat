

def unpack(l):
    for el in l:
        if not isinstance(el, basestring):
            for subl in unpack(el):
                yield subl
        else:
            yield el

def check_contains(x, keyword, exact = False): 
    if exact:
        for word in x.split(","):
            return keyword == word
    else:
        for word in x.split(","):
            return keyword in word
            
            
def check_contains_howmany(x, keyword, exact = False): 
    counter = 0
    if exact:
        for word in x.split(","):
            if keyword == word:
                counter += 1
    else:
        for word in x.split(","):
            print word
            if keyword in word:
                counter += 1
    return counter

    