def ex3(assignatura,**codes):
    print("{}".center(62,"=").format(assignatura))
    print("Code".ljust(20) + "Midterm Exam".rjust(15) + "Final Exam".rjust(15) + "Average Grade".rjust(15))
    try:
        total = 0
        ids = len(codes)

        for id, nota in codes.items():
            if not isinstance(nota, list):
                raise ValueError("The values have to be a list of floats")

            if len(nota) != 2:
                raise AssertionError("The list have to contain only two floats")
            for elemento in nota:
                if not isinstance(elemento, float):
                    raise TypeError("Values in list have to be integers")

            mid_exam = round(nota[0],1)
            fin_exam = round(nota[1],1)
            avg_grade = round(float(mid_exam + fin_exam / 2),1)
            total += avg_grade

            print(str(id).ljust(20) + str(mid_exam).rjust(15) + str(fin_exam).rjust(15) + str(avg_grade).rjust(15))
        total_avg = 0
        if codes:
            total_avg = total/ids
            print("="*65)
            print("total".ljust(50) + str(total_avg).rjust(15))

    except Exception as error:
        print(error)
        quit()


ex3("Maths")
ex3("Maths", RT345=[7.15,6.55])
ex3("Maths", RT345=[7.15,6.55], SW432=[5.44,7.63])
#ex3("Maths", RT345=[7.15,6.55], SW432=[5.44,7.63],OT441=[4.35, 6.18])
