from flask import jsonify

def calculate(request):
    first_number = float(request.json.get('firstNumber'))
    second_number = float(request.json.get('secondNumber'))
    operator = request.json.get('operator')

    result = None

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = first_number / second_number
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    return jsonify({'result': result})
