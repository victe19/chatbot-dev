import requests
chatwoot_url = 'http://localhost:8000'
chatwoot_bot_token = 'nqmQPhPMojx6VU2XTfUEHVHC'

'''
    FASTAPI
'''
# from urllib import response
# from fastapi import FastAPI

# app = FastAPI()

# # https://localhost:8000/api/v1/accounts/69496/conversations/1/messages
# # The agent bot can post the generated response back into the widget by calling
# # chatwoot APIs like message_create
# account_id = 6949
# acces_token = 'nqmQPhPMojx6VU2XTfUEHVHC'
# conversation_id = 1

# @app.get('/')
# def helloWorld():
#     return "hello world"

# @app.get('/1')
# def api():
#     return "hola"


# @app.post('/platform/api/v1/agent_bots')
# def create_bot():
#     return "agent creat"

# @app.get('/platform/api/v1/agent_bots')
# def list_agentBots():
#     agent_dict = {}
#     return agent_dict


# @app.post('/api/v1/accounts/69496/conversations/1/messages')
# def create_message():
#     return "hola em dic victor19"

# @app.post('/message')
# def create_message():
#     return {'data': "message is created"}
''''''


'''
    TRY TO CONNECT WITH HTTP METHODS TO APP.CHATWOOT.COM (SIGN_IN)
'''
import http.client
import json
staging = ''

conn = http.client.HTTPSConnection('chatwoot.com',80, timeout=10)
payload = json.dumps({
  "account_name": "Victor.Arauzo",
  "email": "victe19@gmail.com"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", "/platform/api/v1/accounts/{account_id}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

''''''


'''
    SUCCESS CONNECTION TO JOPURNAL DEV 
'''
# import http.client

# connection = http.client.HTTPSConnection("www.journaldev.com")
# connection.request("GET", "/")
# response = connection.getresponse()
# print("Status: {} and reason: {}".format(response.status, response.reason))

''''''