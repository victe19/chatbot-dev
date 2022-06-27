import requests
import json

headers = {
      'Content-Type': 'application/json',
      'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
    }

def setup(self):

  print("Interacting with the API")
  self.api_access_token = 'nqmQPhPMojx6VU2XTfUEHVHC'
  self.account_id = 69496
  self.inbox_id = 12939
  self.url = 'http://app.chatwoot.com' 
  self.outgoing_url = 'https://chatbot-dev-a51e0.web.app/'
  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

def login():

  staging = 'http://app.chatwoot.com'
  payload = json.dumps({
    "email": "victe19@gmail.com",
    "password": "Chatwoot@original19"
  })    

  url = f"{staging}/auth/sign_in"
  response = requests.request("POST", url, headers=headers, data=payload)

  
  # comprobar el status code
  # if statuscode == 200
  
  # else:
  #   raise Exception 

  return response.text


def create_contact(self):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/contacts'

  payload = json.dumps({
    "inbox_id": self.inbox_id,
    "name": "Daniel",
    "email": "victe22@gmail.com",
    "phone_number": "+16175551215",
    "identifier": "4",
    "custom_attributes": {}
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  json_response_dict = response.json()
  print(json_response_dict)
  # self.source_id =str(json_response_dict['payload']['contact_inbox']['source_id'])


def create_conversation(self):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations'

  payload = json.dumps({
    "source_id": self.account_id,
    "inbox_id": 12939,
    "contact_id": 3,
    "additional_attributes": { },
    "status": "open",
    "assignee_id": 457,
    "team_id": "string"
  })

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)


def create_agent_bot(self):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/agent_bots'

  payload = json.dumps({
    "name": "victe",
    "description": "joke enginner",
    "outgoing_url": 'https://chatbot-dev-a51e0.web.app/'
  })

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)



def list_agent_bots(self):
  """
  Create an agent bot in the account

  """
  url = f'https://app.chatwoot.com/api/v1/accounts/69496/agent_bots'

  response = requests.request("GET", url, headers=headers)
  print(response.text)


def get_agent_bot_details(self):

  url = f'https://app.chatwoot.com/platform/api/v1/agent_bots/457'

  response = requests.request("GET", url, headers=headers)
  print(response.text)


def get_open_conversations():

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations'
  response_open= requests.request("GET", url, headers=headers)

  open_conversations = json.loads(response_open.text)
  payload_list = open_conversations['data']['payload']
  open_id_list = [payload['id'] for payload in payload_list]

  return open_id_list


def get_new_conversations():

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations'

  data = json.dumps({ 
      "status": 'pending'
  })  

  response_pending = requests.request("GET", url, headers=headers, data=data)

  pending_conversations = json.loads(response_pending.text)
  payload_list = pending_conversations['data']['payload']
  pending_id_list = [payload['id'] for payload in payload_list]
  
  return pending_id_list
  # return pending_conversations


def post_exit_status(conversation_id: int):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations/{conversation_id}/toggle_status'

  data = json.dumps({ 
      "status": 'resolved'
  })  

  response_pending = requests.request("POST", url, headers=headers, data=data)

  # return pending_id_list


def assinge_conversations(conversation_id: int):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations/{conversation_id}/assignments'

  data = json.dumps({
    "assignee_id": 63149,
    "team_id": 0
  })  

  response_pending = requests.request("POST", url, headers=headers, data=data)
  

def get_all_conversations():
  open_conversations = get_open_conversations()
  new_conversations = get_new_conversations()

  for conversation in new_conversations:
    assinge_conversations(conversation)

  return open_conversations + new_conversations




def get_messages_from_conversation(inbox: str):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations/{inbox}/messages'

  response = requests.request("GET", url, headers=headers)
  print(f"Status code --> {response.status_code}")
  message_meta = json.loads(response.text)
  message_list = message_meta["payload"]
  last_message_json = message_list[-1]
  if last_message_json['message_type'] == 0:
      return last_message_json['content']


def post_messages_to_conversation(message: str, inbox: str):

  url = f'https://app.chatwoot.com/api/v1/accounts/69496/conversations/{inbox}/messages'

  payload = json.dumps({ 
    "content": message, 
    "message_type": "outgoing", 
    "content_attributes": { }
  })  

  response = requests.request("POST", url, headers=headers, data=payload)
  # print(f"Response Server: {response.status_code}")

# class ConversationAPIBehavior():

#   def on_start(self):
#     print("Interacting with the API")
#     self.api_access_token = 'nqmQPhPMojx6VU2XTfUEHVHC'
#     self.account_id = 69496
#     self.inbox_id = 12939
#     self.url = 'http://app.chatwoot.com' 
#     self.outgoing_url = 'https://chatbot-dev-a51e0.web.app/'

#   def interact_with_conversation_api(self):
#     login(self)
#     get_open_conversations(self)
#     message = get_messages_from_conversation()
#     # self.contact_source_id = create_contact(self)
#     # self.converation_id = create_conversation(self)
#     # self.create_message = create_message(self)
#     # self.recive_message = recive_message(self)
#     # self.agent_bot_id = create_agent_bot(self)
#     # self.create_agent_bot = list_agent_bots(self)
#     # self.create_agent_bot = get_agent_bot_details(self)
#     return message

# if __name__ == '__main__':
#   ConversationAPIBehavior().on_start()
#   ConversationAPIBehavior().interact_with_conversation_api()