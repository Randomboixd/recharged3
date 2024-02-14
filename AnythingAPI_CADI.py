# Custom anythingapi dataset interpreter (CADI) for AnythingAPI.

import json
import os
import random

print("CADI> Attempting to load datasets ./CADI-dataset")

global scenarios
global chars

scenarios = []
chars = []

for file in os.listdir("./CADI-dataset"):

    with open(f"./CADI-dataset/{file}", "r") as f:
        content = json.load(f)

    content_type = content["dataset-type"]

    if content_type == "char":
        for char in content["char"]:
            chars.append(char)

    elif content_type == "scenario":

        for scenario in content["scenarios"]:
            scenarios.append(scenario)
    else:
        print(f"CADI> Unrecognized dataset type in ./CADI-dataset/{file}! ({content_type})")

print(f"CADI> Loading finished! We have {len(scenarios)} scenarios and {len(chars)} characters loaded!")

class Imported_Code: # These functions are imported from anythingapi's replit page.
    def getChar():
        the_ultimate_choice = random.choice(chars) 
        return {
            "name": the_ultimate_choice["name"],
            "img": the_ultimate_choice["img"]
        }
    
    def makeScenario():
        scenario = random.choice(scenarios)
  
        if scenario["chars"] == 1:
            char1 = Imported_Code.getChar()
            scenarioText = scenario["text"].format(char1=char1["name"])
            return {
                "status": "done",
                "chars": scenario["chars"],
                "text": scenarioText,
                "imgsArr": [char1["img"], scenario["img"]],
                "imgsOneln": f"{char1['img']}   {scenario['img']}"
            } 


        elif scenario["chars"] == 2:
            char1 = Imported_Code.getChar()
            char2 = Imported_Code.getChar()
            scenarioText = scenario["text"].format(char1=char1["name"], char2=char2["name"])
            return {
                "status": "done",
                "chars": scenario["chars"],
                "text": scenarioText,
                "imgsArr": [char1["img"], char2["img"], scenario["img"]],
                "imgsOneln": f"{char1['img']}   {char2['img']}   {scenario['img']}"
            }
        
        else:
            char1 = Imported_Code.getChar()
            char2 = Imported_Code.getChar()
            char3 = Imported_Code.getChar()
            scenarioText = scenario["text"].format(char1=char1["name"], char2=char2["name"], char3=char3["name"])
            return {
            "status": "done",
            "chars": scenario["chars"],
            "text": scenarioText,
            "imgsArr": [char1["img"], char2["img"], char3["img"], scenario["img"]],
            "imgsOneln": f"{char1['img']}   {char2['img']}   {char3['img']}  {scenario['img']}"
            }

class ANYTHINGAPI_RESPONSE:

    def __init__(self, response) -> None:
        self.status = response["status"]
        self.chars = response["chars"]
        self.text = response["text"]
        self.imgsArr = response["imgsArr"]
        self.imgsOneln = ""
        for x in self.imgsArr:
            self.imgsOneln += x + " "
        self.raw = response

class CADI:

    def __init__(self):
        pass

    def get(self):
        response = Imported_Code.makeScenario()
        obj = ANYTHINGAPI_RESPONSE(response)
        return obj

