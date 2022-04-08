import requests
import json


def login(self):
  """
  Login to chatwoot a new Contact

  Returns:
      _type_: _description_

  """ 

  staging = 'http://app.chatwoot.com'

  payload = json.dumps({
    "email": "victe19@gmail.com",
    "password": "Chatwoot@original19"
  })

  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

  url = f"{staging}/auth/sign_in"
  response = requests.request("POST", url, headers=headers, data=payload)

  return response.text
  
  # comprobar el status code
  # if statuscode == 200
  
  # else:
  #   raise Exception 


def create_contact(self):
  """
  Create a new Contact

  Returns:
      _type_: _description_

  """ 
  url = f'https://app.chatwoot.com/api/v1/accounts/{self.account_id}/contacts'
  
  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

  payload = json.dumps({
    "inbox_id": self.inbox_id,
    "name": "carles",
    "email": "victe21@gmail.com",
    "phone_number": "+16175551214",
    "identifier": "3",
    "custom_attributes": {}
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  json_response_dict = response.json()
  self.source_id =str(json_response_dict['payload']['contact_inbox']['source_id'])


def create_conversation(self):
  """
  Create a new conversation
  
  Returns:
      _type_: _description_

  """  
  url = f'https://app.chatwoot.com/api/v1/accounts/{self.account_id}/conversations'

  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

  payload = json.dumps({
    "source_id": self.source_id,
    "inbox_id": self.inbox_id,
    "contact_id": 3,
    "additional_attributes": { },
    "status": "open",
    "assignee_id": "string",
    "team_id": "string"
  })

  response = requests.request("POST", url, headers=headers, data=payload)



def create_message(self):
  """
  Create a new message

  Returns:
      _type_: _description_

  """ 
  pass


# 4. RECIVE A MESSAGE 
def recive_message(self):

  pass


# 5. CREATE AGENT BOT
def create_agent_bot(self):
  """
  Create an agent bot in the account

  """
  url = f'https://app.chatwoot.com/api/v1/accounts/69496/agent_bots'

  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

  payload = json.dumps({
    "name": "victe",
    "description": "joke enginner",
    "outgoing_url": 'https://chatbot-dev-a51e0.web.app/'
  })

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)


# 6. LISTS AGENT BOTS
def list_agent_bots(self):
  """
  Create an agent bot in the account

  """
  url = f'https://app.chatwoot.com/api/v1/accounts/69496/agent_bots'

  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

  response = requests.request("GET", url, headers=headers)
  print(response.text)


# 7. LISTS AGENT BOTS
def get_agent_bot_details(self):
  """
  Create an agent bot in the account

  """
  url = f'https://app.chatwoot.com/platform/api/v1/agent_bots/457'

  headers = {
    'Content-Type': 'application/json',
    'api_access_token': 'nqmQPhPMojx6VU2XTfUEHVHC'
  }

  response = requests.request("GET", url, headers=headers)
  print(response.text)



class ConversationAPIBehavior():

  def on_start(self):
    print("Interacting with the API")
    self.api_access_token = 'nqmQPhPMojx6VU2XTfUEHVHC'
    self.account_id = 69496
    self.inbox_id = 12939
    self.url = 'http://app.chatwoot.com' 
    self.outgoing_url = 'https://chatbot-dev-a51e0.web.app/'

  def interact_with_conversation_api(self):
    login(self)
    # self.contact_source_id = create_contact(self)
    # self.converation_id = create_conversation(self)
    # self.create_message = create_message(self)
    # self.recive_message = recive_message(self)
    # self.agent_bot_id = create_agent_bot(self)
    self.create_agent_bot = list_agent_bots(self)
    # self.create_agent_bot = get_agent_bot_details(self)

if __name__ == '__main__':
  ConversationAPIBehavior().on_start()
  ConversationAPIBehavior().interact_with_conversation_api()