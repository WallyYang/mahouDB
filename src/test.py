def err(a, b):
    raise Exception("%s != %s" % (a, b))

def cmp(a, b):
    if type(a) != type(b):
        err(a, b)
    if isinstance(a, int):
        if a != b:
            err(a, b)
    elif isinstance(a, str):
        if a != b:
            err(a, b)
    elif isinstance(a, list):
        cmp_list(a, b)
    elif isinstance(a, tuple):
        cmp_list(a, b)
    elif isinstance(a, dict):
        cmp_dict(a, b)
    else:
        if a != b:
            err(a, b)

def cmp_list(a, b):
    if len(a) != len(b):
        err(a, b)
    for i in range(len(a)):
        cmp(a[i], b[i])

def cmp_dict(a: dict, b: dict):
    if len(a) != len(b):
        err(a, b)
    cmp_list(list(a.keys()), list(b.keys()))
    for k in list(a.keys()):
        cmp(a[k], b[k])
