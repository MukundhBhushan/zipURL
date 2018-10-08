from hashids import Hashids
from math import floor
import string

#converting string to integers
def toBase10(__str, b = 2):
    base = string.digits + string.ascii_letters #contains all the alphabets and numbers from 0 to 9
    res = 0
    for i in range(len(__str)):
        res = b * res + base.find(__str[i])
    return res


def short(__input): #generating unique ids for the input
    res=[]
    pk = toBase10(__input)
    domain = "<hosting site url>"

    hashids = Hashids(salt='this is my salt', min_length=6)
    link_id = hashids.encode(pk)
    url = 'http://{domain}/{link_id}'.format(domain=domain, link_id=link_id)
    res.append(url)
    res.append(link_id)
    return(res)
