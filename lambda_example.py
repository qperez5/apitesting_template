# Functional programming:  El hecho de utilizar funciones como objetos, variables.
# lambda: capacidad de definir funciones sin nombre  de usar y tirar.  Da soporte o facilita la programacion funcional
def operate_numbers(a, b, operation):
    return operation(a, b)


sum = lambda a, b: a + b
print(operate_numbers(2, 2, sum))
print(operate_numbers(2, 2, lambda a, b: a - b))