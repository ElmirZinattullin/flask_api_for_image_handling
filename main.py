import os

from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

from your_ai_model.ai_model import ModelAI
from config import UPLOAD_FOLDER, RESULT_FOLDER, WEIGHS_PATH

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Разрешенные расширения файлов

result_url = "/result"

def allowed_file(filename):
    """Проверка расширения файла"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

ai_photo_interpreter = ModelAI(weights_path=WEIGHS_PATH)

@app.post("/handle_photo")
def photo_handle_route():
    session = request.args.get('session')
    if not session:
        return jsonify({'error': 'query param "session: is required'}), 400

    if request.method == 'POST':
        # Проверка наличия файла в запросе
        if 'photo' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['photo']

        if not file or  file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        filename = secure_filename(file.filename)

        if not allowed_file(filename):
            return jsonify({'error': 'Invalid file extension'}), 400


        filepath = UPLOAD_FOLDER / filename
        file.save(filepath)


        try:
            # запускаем обработку фотографии через нейронку
            result_data, image_name = ai_photo_interpreter.get_result(session, filepath)
            file_url = result_url + "/" + image_name
            result = {"result_data": result_data, "image_url": file_url}
            return jsonify(result), 200  # Возвращаем результат
        except Exception as e:
            return jsonify({'error': str(e), 'filename': filename}), 500  # Обработка ошибок


@app.get(result_url + "/<filename>")
def result_photo_route(filename: str):

    # роут для отдачи файлов лучше через nginx

    filepath = RESULT_FOLDER / f"{filename}"

    if not os.path.exists(filepath):
        return jsonify({'error': f'File "{filename}.jpg" not found'}), 404

    if not os.path.isfile(filepath):
        return jsonify({'error': f'File "{filename}.jpg" not found'}), 404

    try:
        return send_file(filepath, mimetype='image/jpeg')  # Отправляем файл
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)