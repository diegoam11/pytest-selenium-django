from django.shortcuts import render

def calculadora(request):
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operacion = request.POST.get('operacion')

            if operacion == 'sumar':
                resultado = num1 + num2
            elif operacion == 'restar':
                resultado = num1 - num2
            elif operacion == 'multiplicar':
                resultado = num1 * num2
            elif operacion == 'dividir':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    error = "No se puede dividir entre cero."
        except ValueError:
            error = "Entrada no válida."

    return render(request, 'operaciones/calculadora.html', {'resultado': resultado, 'error': error})
