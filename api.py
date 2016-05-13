from flask import Flask,request
from flask.ext import restful
import requests
import json

app = Flask(__name__)
api = restful.Api(app)

def query(query_id,query_type,query_num,query_attributes='Id,AA.AuId,AA.AfId,F.FId,J.JId,C.CId,RId'):# query(2140251882,'Id',10000)
    url_head = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr='
    url_type = query_type
    url_id = str(query_id)
    url_num = str(query_num)
    url_attributes = 'attributes='+query_attributes
    url_key = 'subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
    url = url_head+url_type+'='+url_id+'&count='+url_num+'&'+url_attributes+'&'+url_key
    response = requests.get(url)
    return json.loads(response.content)['entities']

class BOP(restful.Resource):


    def get(self):
        self.id1 = request.args.get('id1')
        self.id2 = request.args.get('id2')

        return 



api.add_resource(BOP, '/')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
