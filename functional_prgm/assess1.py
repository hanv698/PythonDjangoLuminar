isl=[
    {"team":"Mumbai City","mp":16,"won":10,"drawn":4,"loss":2,"gf":25,"ga":11,"gd":14,"pts":34},
    {"team":"ATK","mp":16,"won":10,"drawn":3,"loss":3,"gf":22,"ga":10,"gd":12,"pts":33},
    {"team":"Goa","mp":16,"won":5,"drawn":8,"loss":3,"gf":24,"ga":19,"gd":5,"pts":23},
    {"team":"Hyderabad","mp":16,"won":5,"drawn":8,"loss":3,"gf":20,"ga":16,"gd":4,"pts":23},
    {"team":"Northeast United","mp":16,"won":5,"drawn":8,"loss":3,"gf":21,"ga":20,"gd":1,"pts":23},
    {"team":"Bengaluru","mp":17,"won":4,"drawn":7,"loss":6,"gf":19,"ga":21,"gd":-2,"pts":19},
    {"team":"Jameshedpur","mp":16,"won":4,"drawn":6,"loss":6,"gf":15,"ga":19,"gd":-4,"pts":18},
    {"team":"Chennai Indians","mp":16,"won":3,"drawn":8,"loss":5,"gf":11,"ga":16,"gd":-5,"pts":17},
    {"team":"East Bengal","mp":16,"won":3,"drawn":7,"loss":6,"gf":14,"ga":21,"gd":-7,"pts":16},
    {"team":"Kerala Blasters","mp":16,"won":3,"drawn":6,"loss":7,"gf":20,"ga":27,"gd":-7,"pts":15},
    {"team":"Odisha","mp":15,"won":1,"drawn":5,"loss":9,"gf":14,"ga":25,"gd":-11,"pts":8}
]

from functools import reduce

point_high=reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["pts"],isl)))
print("High score:",point_high)

point_low=reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["pts"],isl)))
print("Low score:",point_low)

high_gf=reduce(lambda gf1,gf2:gf1 if gf1>gf2 else gf2,list(map(lambda team:team["gf"],isl)))
print("Highest goal faced:",high_gf)

low_gf=reduce(lambda gf1,gf2:gf1 if gf1<gf2 else gf2,list(map(lambda team:team["gf"],isl)))
print("Lowest goal faced:",low_gf)