import requests
import time
from notion.client import NotionClient

#New Way using Notion-py
client = NotionClient(token_v2="v02%3Auser_token_or_cookies%3ATZk6ioUrv7FA05gGmRTfsnK4CZW1EaN7PCRxnuk79xxcmFHTb8mYg5PB1h-hY_spKbeZ3v0Iaj9O3BD48_puvatBczvFWt9Pss03VcQCe_Or3pML0CPfWvXib7DEHwUqcUV9")

page = client.get_block("https://www.notion.so/NotionGPT-fb413b6135b04b6593bdd228e4b02dfa")

def testCallback(record):
    record.title = record.title.replace("WOW", "")
    print(record.title)

page.add_callback(testCallback)

for i in range(10):
    page.refresh()
    time.sleep(1)
    
#Old way of requesting the Notion API
# url = "https://api.notion.com/v1/pages/4c0e4676438c4cefae642c2c748de620"

# headers = {
#     "accept": "application/json",
#     "Notion-Version": "2022-06-28",
#     "Authorization": "Bearer " + "secret_ijztiJ97FCs2ibsFYC9IvmNGRdEY1JoYhqsHIjCSPT6"
# }

# response = requests.get(url, headers=headers)

# print(response.text.encode('utf-8'))
