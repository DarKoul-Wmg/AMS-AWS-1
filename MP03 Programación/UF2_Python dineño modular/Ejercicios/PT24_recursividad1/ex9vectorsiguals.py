def vectors_iguals(vec1,vec2):
    if len(vec1) == 0 and len(vec2) == 0:
        return True
    else:
        if vec1[-1] == vec2[-1]:
            return vectors_iguals(vec1[:-1],vec2[:-1])
        else:
            return False


#vec1 = (3,4)
vec1 = (3,4,5,6)
vec2 = (3,4,5,6)

print(vectors_iguals(vec1,vec2))
