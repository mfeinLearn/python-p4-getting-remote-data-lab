import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # sends a GET request to the URL passed in on initialization. This method should return the body of the response.
        URL = self.url

        response = requests.get(URL)
        return response.content


    def load_json(self):
        
        # should use get_response_body to send a request, 
        # then return a Python list made up of data converted from the response of that request.

        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            print('Output: ', program)
            
            programs_list.append(program)

        return programs_list

# get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
# get_requester.load_json()
# #=> [{"name"=>"Daniel", "occupation"=>"LG Fridge Salesman"}, {"name"=>"Joe", "occupation"=>"WiFi Fixer"}, {"name"=>"Avi", "occupation"=>"DJ"}, {"name"=>"Howard", "occupation"=>"Mountain Legend"}]