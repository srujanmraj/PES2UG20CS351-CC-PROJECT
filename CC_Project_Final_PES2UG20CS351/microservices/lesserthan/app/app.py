from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import  Api, Resource

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
#api = Api(app)

# class Addition(Resource):
#     def get(self,number_1,number_2):
#         return str(float(number_1)+float(number_2))

# api.add_resource(Addition,"/<int:number_1>/<int:number_2")

@app.route("/<int:number_1>/<int:number_2>", methods=['POST', 'GET'])
def lsthan(number_1,number_2):
    if number_1<number_2:
        return 'True'
    else:
        return 'False'
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )