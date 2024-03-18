from dataclasses import dataclass 

first_name = (input("Please enter your First name; "))
Last_name = str(input("Please enter your last name: "))
Age = int(input("Please enter your age: "))
Weight = float(input("Please enter your weight in Kilograms(Kg): "))
Height = float(input("Enter your height in centimetres(cm): "))
Gender = input("Is the person male or female?: ")


class Person:
    @dataclass

    first_name : str
    Last_name : str 
    Age : int
    Weight : float
    Height : float
    Gender : str



def Bmi_calculations(Age, Weight, Height, Gender):
    return  (Weight / ((Height/100)**2)) 


def result():
    return f{first_name} {last_name}, 'Your BMI is' {Bmi_calculations}


print(result())

    