def get_name_with_age(name:str, age:int) -> str:
    name_with_age = name + "is this old:" + str(age)
    return name_with_age

print(get_name_with_age("robert", 50))