# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:45:49 2021

@author: celin
"""


def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("1 - HDL Analysis")
        print("9 - Quit")
        print("3 - LDL Analysis")
        choice = int(input("Make a Choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 3:
            LDL_Driver()
    print(choice)
    return choice


# HDL analysis
def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)


def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value


def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"


def hdl_output(HDL_value, HDL_answer):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_answer))


# LDL Analysis
def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)


def ldl_input():
    ldl_value = int(input(("Enter LDL Value: ")))
    return ldl_value


def ldl_analysis(LDL_value):
    if LDL_value >= 190:
        return "Very high"
    elif 160 <= LDL_value <= 189:
        return "High"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    else:
        return "Normal"


def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_answer))


# Cholesterol Analysis
def C_Driver():
    C_value = c_input()
    C_character = c_analysis(C_value)
    c_output(C_value, C_character)


def c_input():
    c_value = int(input(("Enter Cholesterol Value: ")))
    return c_value


def c_analysis(C_value):
    if C_value >= 240:
        return "High"
    elif 200 <= C_value <= 239:
        return "Borderline High"
    else:
        return "Normal"


def c_output(C_value, C_answer):
    print("The cholesterol value of {} is considered {}".format
          (C_value, C_answer))


if __name__ == "__main__":
    interface()
