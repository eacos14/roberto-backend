from flask import Flask, request, jsonify
from chatgpt import responder

app = Flask(__name__)

@app.route("/consultar", methods=["GET"])
def consultar():
    consulta = request.args.get("consulta", "").strip()
    if not consulta:
        return jsonify({"respuesta": "Consulta vacía."}), 400

    prompt = f"""Sos Roberto, el asistente legal-técnico de la Municipalidad de Florencio Varela. Respondé con claridad, formalidad y precisión legal.
La persona consultó: "{consulta}".
Redactá una respuesta clara, orientativa y útil para el ciudadano.
"""
    try:
        respuesta = responder(prompt)
        return jsonify({"respuesta": respuesta})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
