from . import test
import uuid
from utils import *
import requests

from flask import jsonify, request


from flask import jsonify, request

@test.route('/tes', methods=['GET'])
def tes():
    return jsonify({"msg" : "welcome to my module"})



@test.route('/top_headlines', methods=['GET'])
def top_headlines():
    idb1 = request.args["country"]


    URL = "https://newsapi.org/v2/top-headlines"

    apiKey = "d5cc1ce998724da6976daa48498be007"

    PARAMS = {'country':idb1, 'apiKey': apiKey}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    result = []

    for j in range (0,len('articles')):
         fin = {}
         fin['title'] = data['articles'][j]['title']
         fin['description'] = data['articles'][j]['description']
         fin['image_url'] = data['articles'][j]['urlToImage']
         fin['url'] = data['articles'][j]['url']
         result.append(fin)

    return jsonify({"data":result })


@test.route('/headline_query', methods=['GET'])
def headline_query():
    idb1 = request.args["phrase"]


    URL = "https://newsapi.org/v2/everything"

    apiKey = "d5cc1ce998724da6976daa48498be007"

    PARAMS = {'q':idb1, 'apiKey': apiKey}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    result = []
    for j in range (0,len('articles')):
         fin = {}
         fin['title'] = data['articles'][j]['title']
         fin['description'] = data['articles'][j]['description']
         fin['image_url'] = data['articles'][j]['urlToImage']
         fin['url'] = data['articles'][j]['url']
         result.append(fin)

    return jsonify({ "data":result })








