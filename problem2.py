number_of_students = 26
number_of_chicken = input("Enter # of chicken: ")
number_of_chicken = int(number_of_chicken)
num_pieces_per_student = int(number_of_chicken / number_of_students)
teachers_chicken = number_of_chicken - num_pieces_per_student * number_of_students
print("The students get "+ str(num_pieces_per_student) +" pieces of chicken.")
print("Mr. Fabroa gets "+ str(teachers_chicken) +" pieces of chicken.")