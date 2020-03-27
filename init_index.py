import sys
import requests

es_url = sys.argv[1]
filename = sys.argv[2]

doc_num = 1
with open(filename) as f:
    for line in f:
	url = es_url + '/articles/article'
	data = line
	headers = {'content-type': 'application/json'}
	requests.post(url=url, data=data, headers=headers)
        print('Added document #:\t' + str(doc_num))
        doc_num += 1
