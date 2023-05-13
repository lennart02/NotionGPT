from notion.client import NotionClient
from notion.block import *
import chatGPT
import json

#New Way using Notion-py


#Scans whole Notion page for GPT! and requests the API for a response
def SearchPage(page):
    for child in page.children:
        if(child.title.startswith("GPT!")):
            print(child.title.encode("utf-8"))
            try:
                response = chatGPT.AskGPT3(child.title.replace("GPT!", ""))
            except:
                response = "Chat GPT is not working right now."
            if(len(response) < 600):
                newchild = page.children.add_new(TextBlock, title="Answer: " + response)
                newchild.move_to(child, "after")                
            else:
                #If the response is too long, create a new page and put the response there
                newPage = page.children.add_new(PageBlock, title="Answer")
                newPage.children.add_new(TextBlock, title="Answer: " + response)
            child.title = child.title.replace("GPT!", "User: ")
    
if __name__ == "__main__":
    #searches in every path in the config.json file
    with open("config.json", "r") as f:
        data = json.load(f)
        client = NotionClient(token_v2=data["token"])
        for i in data["pages"]:
            page = client.get_block(i)
            SearchPage(page)

    