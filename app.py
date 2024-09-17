from flask import Flask, jsonify, request

app = Flask(__name__)

# Arquivo JSON que armazenará o status
STATUS_FILE = 'status.json'

# Função para ler o status do arquivo
def read_status():
    with open(STATUS_FILE, 'r') as file:
        return jsonify({"status": file.read()})

# Função para atualizar o status (autenticada com uma chave API simples)
@app.route('/update_status', methods=['POST'])
def update_status():
    api_key = request.headers.get('API-Key')
    
    # Autenticação simples usando uma chave de API
    if api_key != 'SUA_API_KEY_AQUI':
        return jsonify({"error": "Unauthorized"}), 401
    
    new_status = request.json.get('status')
    
    # Atualiza o status no arquivo
    if new_status in ['online', 'offline']:
        with open(STATUS_FILE, 'w') as file:
            file.write(new_status)
        return jsonify({"message": "Status updated successfully!"})
    else:
        return jsonify({"error": "Invalid status"}), 400

# Rota para verificar o status
@app.route('/status', methods=['GET'])
def get_status():
    return read_status()

if __name__ == '__main__':
    app.run(debug=True)
