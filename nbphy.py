def displacement(val, unit: str):
    if unit=="km":
        return val/1000
    elif unit=="m":
        return val
    elif unit=="dm":
        return val*10
    elif unit=="cm":
        return val*100
    elif unit=="mm":
        return val*1000
    elif unit=="μm":
        return val*1000000
    elif unit=="nm":
        return val*1000000000
    raise NotImplementedError("unknown unit")
def time(val, unit: str):
    if unit=="y":
        return val/31536000
    elif unit=="d":
        return val/86400
    elif unit=="h":
        return val/3600
    elif unit=="min":
        return val/60
    elif unit=="s":
        return val
    elif unit=="ms":
        return val*1000
    elif unit=="μs":
        return val*1000000
    raise NotImplementedError("unknown unit")
def velocity(val, unit: str):
    if unit=="m/s":
        return unit
    elif unit=="km/h":
        return unit/3.6
    raise NotImplementedError("unknown unit")
