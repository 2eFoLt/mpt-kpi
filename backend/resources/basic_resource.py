from flask_restful import Resource, reqparse

docs = {}

class BasicResource(Resource):
    def get(self, source_id: int) -> dict:
        return {source_id: docs.get(source_id)}

    # FOR UPDATE
    def put(self, source_id: int):
        docs[source_id] = source_id
        return {source_id: source_id}

    # FOR CREATE
    def post(self, source_id: int):
        docs[source_id] = source_id
        return {source_id: source_id}, 201
