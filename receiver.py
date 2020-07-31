import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('./cat_small.jpg','rb')})

pp.pprint(resp.json())