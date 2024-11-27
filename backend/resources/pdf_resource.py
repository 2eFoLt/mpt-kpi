from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask_restful import Resource, reqparse
from flask import request

#TODO: try rewriting using reqparse, do get() part with file link for downloading and delete()
class PDFResource(Resource):
    def post(self):
        file = request.files.get('uploaded_file')
        print(file.mimetype, file.filename, secure_filename(file.filename))
        file.save(dst="docs/"+file.filename)
        return {'file': 'saved:OK'}, 201