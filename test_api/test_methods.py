import requests
import json

"""Sample methods to check the rest api crud operations"""


def test_get():
    r = requests.get('https://httpbin.org/get')
    a= r.headers
    assert a['Content-Type'] == 'application/json'


def test_post():
    data = {'key1':'value1','key2':'value2'}
    r = requests.post('https://httpbin.org/post',data=data)
    a = json.loads(r.text)
    assert a['form']['key1'] == 'value1'


def test_put():
    data = {'key1':'value1','key2':'value2','key3':'value3'}
    r = requests.put('https://httpbin.org/put',data=data)
    a = json.loads(r.text)
    assert a['form']['key3'] == 'value3'


def test_x_delete():
    r = requests.delete('https://httpbin.org/delete')
    a = r.headers
    assert a['Content-Type'] == 'application/json'

