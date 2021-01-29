employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"danie","salary":20000,"exp":2},
    1002:{"id":1002,"name":"jack","salary":45000,"exp":4},
    1003:{"id":1003,"name":"jerry","salary":35000,"exp":3}
}

def emp(**kwargs):
    #print(kwargs)
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])

emp(id=1000,prop="salary")