# -*- coding: utf-8 -*-

def input_celsius_value ():
    celsius_value = float (input ("변환하고 싶은 섭씨 온도를 입력해 주세요:"))
    return float(celsius_value)

def convert_celsius_fahrenheit (celsius_value):
    a = ((9/5)*celsius_value+32)
    return a

def print_fahrenheit_value (celsius_value, fahrenheit_value):
    print("섭씨온도:" , celsius_value)
    print("화씨온도:" , fahrenheit_value)

def main():
    print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    celsius_value = input_celsius_value ()
    fahrenheit_value = convert_celsius_fahrenheit (celsius_value)
    print_fahrenheit_value (celsius_value, fahrenheit_value)
    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()
