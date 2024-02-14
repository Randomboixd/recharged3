import sqlite3
import json
import time
from transactionlib import create_positive_transaction


global registry 

with open("achievement.registry", "r") as f:
    reg = json.load(f)
    registry = reg["registry"]

class AssignmentErrors:

    class AlreadyAssigned(Exception):
        pass

    class UnregisteredInRegistry(Exception):
        pass

    class DefinitionError(Exception):
        pass

class Achievement_Models:

    class Achievement_Entry:

        def __init__(self, result):

            self.name = result["name"]
            self.explainer = result["explainer"]
            self.charges = result["charges"]


class Achievement_Management:
    
    def __init__(self, uid: int) -> None:
        self.userid = uid

    def award(self, registryid: str, raiseerror: bool = False) -> None:
        """Awards an achievement if possible. Does nothing if achievement is already given, unless raiseerror is set to True."""

        if registryid not in registry:
            raise AssignmentErrors.UnregisteredInRegistry(f"{registryid} is not defined in achievement.registry!")
        
        achievement = registry[registryid]

        if "name" not in achievement:
            raise AssignmentErrors.DefinitionError(f"name is not defined in {registryid}!")
        
        if "explainer" not in achievement:
            raise AssignmentErrors.DefinitionError(f"explainer is not defined in {registryid}!")
        
        if "charges" not in achievement:
            charges = 0
        else:
            charges = achievement["charges"]

        connection = sqlite3.connect("electricity.db")
        cursor = connection.cursor()

        _hasachievement = cursor.execute("SELECT * FROM achievementd WHERE userid = ? AND achievementid = ?", (self.userid, registryid,)).fetchone()

        if _hasachievement != None and raiseerror:

            connection.close()
            raise AssignmentErrors.AlreadyAssigned(f"Achievement {registryid} is already registered to user {self.userid}!")
        
        elif _hasachievement != None:

            connection.close()
            return
        
        current_unix = int(time.time())

        cursor.execute("INSERT INTO achievementd VALUES(?,?,?)", (self.userid, registryid, current_unix,))

        connection.commit()
        connection.close()

        create_positive_transaction(self.userid, f"Achievement earned: {achievement['name']}", charges)
        
        return
    
class Achievement_Registry:

    def __init__(self):
        pass

    def getentry(self, registryentry:str):
        """Get an entry from the registry, and return it as a python object"""

        if registryentry not in registry:
            raise AssignmentErrors.UnregisteredInRegistry(f"{registryentry} is not defined in achievement.registry!")

        
        achievement = registry[registryentry]

        return Achievement_Models.Achievement_Entry(achievement)


        