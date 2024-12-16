from flask_restful import Resource, reqparse
from flask import request
from services.employees_generator import Employee, employees_list


# parser = reqparse.RequestParser()
# (
#     parser.add_argument(argument) for argument in
#     'id first_name last_name surname job_id phone email'.split()
# )

class EmployeesResource(Resource):
    def get(self) -> dict:
        return [employee._asdict() for employee in employees_list]

    def post(self) -> dict:
        args = request.json
        #args = parser.parse_args()
        print(args)
        employee = Employee(
            id=args['id'],
            first_name=args['first_name'],
            last_name=args['last_name'],
            surname=args['surname'],
            job_id=args['job_id'],
            phone=args['phone'],
            email=args['email'],
        )
        employees_list.append(employee)
        return employees_list[-1]._asdict()
