
# for x in range(1, 4):
#     print(int((str((float(x))))))

# fl = "A"
# ll = "Z"
# x = ord(ll)-ord(fl)


# Check next number plate
def increment_char(x):
    next_letter = chr(ord(x)+1) if x != "Z" else "A"
    print("next_letter", next_letter)
    return next_letter
# print(increment_char("Z"))


def increment_str(x):
    lpart = x.rstrip("Z")
    print("lpart", lpart)
    print("len(x)", len(x))
    print("len(lpart)", len(lpart))
    num_replacements = len(x) - len(lpart)
    print("num_replacements", num_replacements)
    new_s = lpart[:-1] + increment_char(lpart[-1]) if lpart else "A"
    print("new_s", new_s)
    new_s += "A" * num_replacements
    print("new_s", new_s)
    return new_s


# print(increment_str("KAA00YZ"))

# write an application that can take in two Kenyan license plates (kxx-00x)as parameters and find how many plates have been registered between the two plates.
# Example:
# KAA000A and KAA000B = 1
# KAA000A and KAA000Z = 25
# KAA000A and KAA001A = 26


# def difference_char(a, b):
#     return ord(b)-ord(a)


# print(difference_char("A", "Z"))

list1 = []


# def get_total_values(n):
#     total_value = [int(value) * 10**place for place,
#                    value in enumerate(str(n)[::-1])]
#     return total_value


# print(get_total_values(10))


def subtract_plates(a, b):
    # removes K because its constant
    a = a[1:]
    b = b[1:]
    print("remove K, ", a+" ,"+b)

    # loops through the a and b subtracting each
    for i, j in zip(a, b):
        list1.append(ord(j)-ord(i))

    print(list1)

    s = [str(i)for i in list1]

    # adding each item to each in the array
    s = 260000*int(s[0])+26000*int(s[1])+2600*int(s[2]) + \
        260*int(s[3])+26*int(s[4])+int(s[5])
    return abs(s)


print(subtract_plates("KAA001A", "KAA000A"))
