
def update_speed(level, triggers):
    t = triggers
    if level == 2:
        t["monster"] = 1
        t["monster2"]= 0
        t["zombie"] = 3
    if level == 3:
        t["zombie"] = 2
        t["monster"] = 3
    if level == 4:
        t["zombie"] = 1
        t["monster"] = 2
    if level == 5:
        t["zombie"] = 3
        t["monster"] = 4
    if level == 6:
        t["zombie"] = 2
        t["monster"] = 4
        t["monster2"] = 4
    if level == 7:
        t["zombie"] = 2
        t["monster"] = 3
        t["monster2"] = 4
    if level == 8:
        t["zombie"] = 2
        t["monster"] = 3
        t["monster2"] = 3
    return t
