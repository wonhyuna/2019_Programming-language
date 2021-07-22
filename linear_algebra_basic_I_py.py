def vector_size_check(*vector_variables):
    value = 0
    last_value = 0
    for vector in vector_variables:
        value = len(vector)
        if last_value == 0:
            last_value = len(vector)
        else:
            if value != last_value:
                return False
        last_value = len(vector)
    return True



def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    result = vector_variables[0]
    number = 0
    for vector in vector_variables:
        if number==0:
            number += 1
            continue
        for i in range(len(vector)):
            result[i] = result[i]+vector[i]
    return result



def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    result = vector_variables[0]
    number = 0
    for vector in vector_variables:
        if number==0:
            number += 1
            continue
        for i in range(len(vector)):
            result[i] = result[i]-vector[i]
    return result




def scalar_vector_product(alpha, vector_variable):
    for i in range(len(vector_variable)):
        vector_variable[i] = vector_variable[i] * alpha
    return vector_variable




def matrix_size_check(*matrix_variables):
    value = 0
    last_value = 0
    for vector in matrix_variables:
        value = len(vector)
        if last_value == 0:
            last_value = len(vector)
        else:
            if value != last_value:
                return False
        last_value = len(vector)
    return True





def is_matrix_equal(*matrix_variables):
    for matrix in matrix_variables:
        if matrix != matrix_variables[0]:
            return False
    return True






def matrix_addition(*matrix_variables):
    if vector_size_check(*matrix_variables) == False:
        raise ArithmeticError

    result = [[0 for col in range(len(matrix_variables[0][0]))] for row in range(len(matrix_variables[0]))]
    for vector in matrix_variables:
        for i in range(len(vector)):
            for j in range(len(vector[i])):
                result[i][j] = result[i][j] + vector[i][j]
    return result







def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    result = [[0 for col in range(len(matrix_variables[0][0]))] for row in range(len(matrix_variables[0]))]
    index = 0
    for matrix in matrix_variables:
        if index == 0:
            index += 1
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    result[i][j] = result[i][j] + matrix[i][j]
            continue
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result[i][j] = result[i][j] - matrix[i][j]
    return result







def matrix_transpose(matrix_variable):
    return [[element for element in i] for i in zip(*matrix_variable)]

#[2, 5] [1, 1] [2, 2]
#[2, 1, 2] [5, 1, 2]






def scalar_matrix_product(alpha, matrix_variable):
    for i in range(len(matrix_variable)):
        for j in range(len(matrix_variable[i])):
            matrix_variable[i][j] = matrix_variable[i][j] * alpha
    return matrix_variable







def is_product_availability_matrix(matrix_a, matrix_b):
    if len(matrix_a[0])==len(matrix_b):
        return True
    else:
        return False
#각자안의개수=큰거여러개개수






def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [[sum(a * b for a, b in zip(row_a, column_b))  for column_b in zip(*matrix_b)] for row_a in matrix_a]
