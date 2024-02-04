from src.graphic import * 
from src.editor.run import * 

def proccessAction (action):
    if (action == 1):
        return showNotes()
    if (action == 2):
        return addNotes()
    if (action == 3):
        return removeNotes()
    
    return "none"


def showNotes():
    show("Omaigad maldito idiota estas viendo notas notisiadas")
    return False

def addNotes():
    return False

def removeNotes():
    return False