def rang_valors(num,rang_min,rang_max):
    if num < rang_min or num > rang_max:
        return False
    elif num == rang_min or num == rang_max:
        return True
    else:
        return rang_valors(num,rang_min + 1,rang_max)



num = 8
rang_min = 1
rang_max = 9

print(rang_valors(num,rang_min,rang_max))
