import requests,json
class omdb:
    def __init__(self,apikey):
        self.apikey=apikey
        self.base_url="http://www.omdbapi.com/"
    def set_param(self,param_code):
        self.param=param_code
    def send_request(self):
        self.params={
            'apikey':self.apikey,
            's':self.param
        }
        self.response=requests.get(self.base_url,self.params)
        return self.response
