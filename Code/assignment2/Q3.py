def grade_calc(grades_in, to_drop):
    grades_in.sort(reverse=True)
    for i in range(to_drop):
        grades_in.pop()
    avg=sum(grades_in)/len(grades_in)
    if 90 <= avg <= 100 :
        grade='A'
    elif 80 <= avg < 90 :
        grade='B'
    elif 70 <= avg < 80 :
        grade='C'
    elif 60 <= avg < 70 :
        grade='D'
    elif avg<60:
        grade='F'
    return grade


