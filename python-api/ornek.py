from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)


# API'nin base URL'i
base_url = "https://passwordinator.onrender.com"

# -?len=18 ( 18 karakterlik şifre oluşturur. 7'den büyük olmalıdır. Varsayılan 12'dir)
class CreatePass(Resource):
    def get(self,lenght):
        url = f"{base_url}/?len={length}"
        response = requests.get(url)
    
        if response.status_code == 200:
            password = response.json().get('data')
            return password
        else:
            return {'error': f'error'}, 500  

# Add URL endpoints
api.add_resource(CreatePass, '/createpassword/<string:lenght>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
    app.run()

