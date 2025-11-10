from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@app.route('/')
def index():
        html = "<head><title>API de Cálculo de Factorial</title></head>" \
        "<body>Para usar utilizar: /calcular/(numero)<h3>Ejemplo: /calcular/5</h3></body>"

        return html

@app.route('/calcular/<int:numero>', methods=['GET'])
def calcular(numero):
    # Calcular factorial
    fact = factorial(numero)

    # Determinar si el factorial es par o impar
    etiqueta = "par" if numero % 2 == 0 else "impar"

    # Construir respuesta JSON
    respuesta = {
        "numero_recibido": numero,
        "factorial": fact,
        "etiqueta": etiqueta
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)
