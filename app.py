from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
IMAGE_FOLDER = os.path.join(os.getcwd(), 'outfit')

@app.route('/api/icon/<icon_id>', methods=['GET'])
def get_icon(icon_id):
    filename = f"{icon_id}.png"
    filepath = os.path.join(IMAGE_FOLDER, filename)
    
    if os.path.exists(filepath):
        return send_from_directory(IMAGE_FOLDER, filename)
    else:
        return jsonify({'error': 'Icon not found'}), 404

if __name__ == '__main__':
    print(f"[INFO] Image folder: {IMAGE_FOLDER}")
    app.run(debug=True)
