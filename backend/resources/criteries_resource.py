from flask_restful import Resource, reqparse
from services.criteries_generator import Criterion, criteries_list


class CriteriesResource(Resource):
    def get(self) -> dict:
        return [criterion._asdict() for criterion in criteries_list]
