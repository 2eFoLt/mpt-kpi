from flask_restful import Resource, reqparse
from services.certificates_generator import Certificate, certificates_list


class CertificatesResource(Resource):
    def get(self) -> dict:
        return [certificate._asdict() for certificate in certificates_list]