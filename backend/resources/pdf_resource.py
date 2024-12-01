import os

from werkzeug.utils import secure_filename
from flask_restful import Resource, abort
from flask import request, send_from_directory

ALLOWED_EXTENSIONS = ['pdf', 'doc', 'docx']


def find_local_file(target_name) -> bool:
    for (root, folder, file_name) in os.walk('docs'):
        if len(file_name) == 0: return False
        if file_name[0] == target_name: return True
    return False

def validate_extension(file_ext) -> bool:
    for ext in ALLOWED_EXTENSIONS:
        if file_ext == ext: return True
    return False

def build_name(file_name, file_ext) -> str: return file_name + '.' + file_ext

class PDFResource(Resource):
    def post(self):
        file = request.files.get('uploaded_file')
        save_filename, save_ext = secure_filename(file.filename).split('.')
        if not validate_extension(save_ext): abort(415)
        if find_local_file(file.filename):
            save_filename += '_copy'
        save_filename = build_name(save_filename, save_ext)
        file.save(dst="docs/"+secure_filename(save_filename))
        return {'file': 'saved:OK'}, 201

    def get(self, filename):
        if find_local_file(filename):
            # Возвращает файл, который открывается в браузере
            # На фронте можно просто дать ссылку на docs/<имя файла>
            # <a href="docs/filo.pdf">File link</a>, должно работать
            return send_from_directory('docs', secure_filename(filename))
        else:
            abort(404)

    def delete(self, filename):
        try:
            os.remove(os.path.join('docs', secure_filename(filename)))
            return {'file': 'deleted:OK'}, 200
        except WindowsError as e:
            print(e)
            abort(404)