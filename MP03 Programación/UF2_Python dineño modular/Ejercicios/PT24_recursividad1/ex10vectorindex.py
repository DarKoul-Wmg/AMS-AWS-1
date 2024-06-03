def index_vector(vec):

    if len(vec) == 0:
        return False

    elif vec[-1] == len(vec)-1:
        resultado = vec[-1]
        return resultado
    else:
        return index_vector(vec[:-1])


vec = (4,3,2,1)
#vec = (4,3,1,2)
print(index_vector(vec))
