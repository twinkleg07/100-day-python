def calculate_love_score(name1,name2):
    names=name1+name2
    lower_names= names.lower()
    
    t=lower_names.count("t")
    r=lower_names.count("r")
    u=lower_names.count("u")
    e=lower_names.count("e")
    first= t+r+u+e
    l=lower_names.count("l")
    o=lower_names.count("o")
    v=lower_names.count("v")
    e=lower_names.count("e")
    second= l+o+v+e
    score=int(str(first)+str(second))
    print(score)

calculate_love_score("kim kardashian","kanye west")