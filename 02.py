import os

try:
    os.makedirs('my_project//settings')
    os.makedirs('my_project//mainapp')
    os.makedirs('my_project//adminapp')
    os.makedirs('my_project//authapp')
except FileExistsError:
    None
