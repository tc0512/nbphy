class Unknown:
    def __repr__(self):
        return "Unknown"
    def __bool__(self):
        return False
    def __contians__(self):
        return False
def displacement(val, unit: str):
    if unit=="km":
        return val*1000
    elif unit=="m":
        return val
    elif unit=="dm":
        return val/10
    elif unit=="cm":
        return val/100
    elif unit=="mm":
        return val/1000
    elif unit=="μm":
        return val/1000000
    elif unit=="nm":
        return val/1000000000
    raise NotImplementedError("unknown unit")
def time(val, unit: str):
    if unit=="h":
        return val*3600
    elif unit=="min":
        return val*60
    elif unit=="s":
        return val
    elif unit=="ms":
        return val/1000
    elif unit=="μs":
        return val/1000000
    raise NotImplementedError("unknown unit")
def velocity(val, unit: str):
    if unit=="m/s":
        return val
    elif unit=="km/h":
        return val*3.6
    raise NotImplementedError("unknown unit")
def density(val, unit: str):
    if unit=="g/cm^3":
        return val*1000
    elif unit=="kg/m^3":
        return val
    raise NotImplementedError("unknown unit")
def force(val, unit: str):
    if unit=="N":
        return val
    raise NotImplementedError("unknown unit")
def pressure(val, unit: str):
    if unit=="Pa":
        return val
    raise NotImplementedError("unknown unit")
def work(val, unit: str):
    if unit=="J":
        return val
def power(val, unit: str):
    if unit=="W":
        return val
    elif unit=="kW":
        return val*1000
def tabular(field: list, row: list):
    table = PrettyTable()
    table.field_names = field
    for i in row:
        table.add_row(i)
    return table
def average(data: list):
    if len(data)==0:
        raise ValueError("list is empty")
    return sum(data)/len(data)
def lever(F1, l1, F2, l2):
    if F1==Unknown():
        return f"F1={F2*l2/l1}"
