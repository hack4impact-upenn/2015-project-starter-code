from app import app


@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'


@app.route('/health', methods=['GET'])
def health():
    return 'OK ;)', 200
