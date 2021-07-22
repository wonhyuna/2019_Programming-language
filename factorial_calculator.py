# -*- coding: utf-8 -*-


def get_factorial_value(integer_value):
    number=1
    for  i in range(1, integer_value+1):
        number=number*i
    return number

def is_positive_number(integer_str_value):
    # '''
    # Input:
    #   - integer_str_value : 숫자형태의 문자열 값
    # Output:
    #   - integer_str_value가 양수일 경우에는 True,
    #     integer로 변환이 안되거나, 0, 음수일 경우에는 flase
    # Examples:
    #   >>> import factorial_calculator as fc
    #   >>> fc.is_positive_number("100")
    #   True
    #   >>> fc.is_positive_number("0")
    #   False
    #   >>> fc.is_positive_number("-10")
    #   False
    #   >>> fc.is_positive_number("abc")
    #   False
    # '''
    try:
        # ===Modify codes below=============
        # 시작전 반드시 'pass'를 지울 것
        if int(integer_str_value) >0:
            result = True
        else:
            result = False
        return result
        # ==================================
    except ValueError:
        return False


def main():
    user_input = 999
    # ===Modify codes below=============
    while(user_input is not 0):
        user_input=input("Input a positive number:")
        if (is_positive_number(user_input)==True):
            print (get_factorial_value(int(user_input)))
        elif (user_input is '0'):
            print("Thank you for using this program.")
            break
        else:
            print("Input again, Please.")

    # ==================================

if __name__ == "__main__":
    main()
