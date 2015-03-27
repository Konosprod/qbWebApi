# -*- coding: utf8 -*-
import requests
import json
import codecs
from requests.auth import HTTPDigestAuth

user=""
password=""
url=""
port=""

def setParam(params):
    global user
    global password
    global url
    global port
    
    user = params['user']
    password = params['password']
    url = params['url']
    port = params['port']

def qbwebapiGet(req):
    global password
    global user
    global port
    global url
    
    return requests.get(url + ":" + port + req, auth=HTTPDigestAuth(user, password))
    
def qbwebapiPost(req, payload):
    global password
    global user
    global port
    global url
    
    return requests.post(url + ":" + port + req, data=payload, auth=HTTPDigestAuth(user, password))
    
def qwebapiPostMEF(req, file):
    global password
    global user
    global port
    global url
    
    files = {'file':('new.torrent', open(file, 'rb'), 'application/x-bittorent')}
        
    return requests.post(url + ":" + port + req, files=files, auth=HTTPDigestAuth(user, password))
    

def checkCredentials(url, user, password):
    ret = False
    
    try:
        response = qbwebapiGet("")
        
        if response.ok:
            ret = True
    except:
        response.raise_for_status()
    
    return ret
    
def getTorrents():
    
    response = qbwebapiGet("/json/torrents")
    
    if response.ok:
        return response.json()
    else:
        return ""
        
def shutdownClient():
 
    qbwebapiGet("/command/shutdown")
    
def getTorrentGenericProperties(torrentHash):
 
    response = qbwebapiGet("/json/propertiesGeneral/" + torrentHash)
    
    return response.json()
   
def getTorrentSpecificProperties(torrentHash):
    
    response = qbwebapiGet("/json/propertiesFiles/" + torrentHash)
    
    return response.json()
   
def getTorrentTrackers(torrentHash):
    response = qbwebapiGet("/json/propertiesTrackers/" + torrentHash)
    
    return response.json()
    
def getGlobalTransfertInfo():
    response = qbwebapiGet("/json/transferInfo")
    
    return response.json()
    
def getPreferences():
    response = qbwebapiGet("/json/preferences")
    
    return response.json()
 
def addTorrent(urls):
    data = ""
    for s in urls:
        data += s + "\n"
        
    response = qbwebapiPost("/command/download/", {'urls' : data})
    
def uploadTorrent(path):
    response = qwebapiPostMEF("/command/upload", path)
    
def addTrackers(torrentHash, trackers):
    data = ""
    
    for s in trackers:
        data += s + "\n"
        
    response = qwebapiPost("/command/addTrackers", {'hash':torrentHash, 'urls' : data})
    
def pauseTorrent(torrentHash):
    response = qbwebapiPost("/command/pause", {'hash':torrentHash})
    
def resumeTorrent(torrentHash):
    response = qbwebapiPost("/command/resume", {'hash':torrentHash})
    
def pauseAll():
    response = qbwebapiPost("/command/pauseall", "")

def resumeAll():
    response = qbwebapiPost("/command/resumeall", "")
    
def deleteTorrents(hashes):
    data = ""
    
    for s in hashes:
        data += s + "|"
        
    response = qbwebapiPost("/command/delete", {'hashes': data})
    
def deleteTorrentsPerm(hashes):
    data = ""
    
    for s in hashes:
        data += s + "|"
    
    response = qbwebapiPost("/command/deletePerm", {'hashes' : data})
    
def recheckTorrent(torrentHash):
    response = qbwebapiPost("/command/recheck", {'hash' : torrentHash})
    
def increaseTorrentPriority(hashes):
    data = ""
    
    for s in hashes:
        data += s + "|"
        
    response = qbwebapiPost("/command/increasePrio", {'hashes' : data})
    
def decreaseTorrentPriority(hashes):
    data = ""
    
    for s in hashes:
        data += s + "|"
        
    response = qbwebapiPost("/command/decreasePrio", {'hashes' : data})
    
def maximalTorrentPriority(hashes):
    data = ""
    
    for s in hashes:
        data += s + "|"
        
    response = qbwebapiPost("/command/topPrio", {'hashes' : data})
    
def minimalTorrentPriority(hashes):
    data = ""
    
    for s in hashes:
        data += s + "|"
    
    response = qbwebapiPost("/command/bottomPrio", {'hashes' : data})
    
def setFilePriority(torrentHash, id, priority):
    response = qbwebapiPost("/command/setFilePrio", {'hash' : torrentHash, 'id' : id, 'priority' : priority})
    
def getGlobalDownloadLimit():
    response = qbwebapiPost("/command/getGlobalDlLimit", "")
    
    return int(response.text)
    
def setGlobalDownloadLimit(limit):
    response = qbwebapiPost("/command/setGlobalDlLimit", {'limit' : limit})
    
def getGlobalUploadLimit():
    response = qbwebapiPost("/command/getGlobalUpLimit", "")
    
    return int(response.text)
    
def setGlobalUploadLimit(limit):
    response = qbwebapiPost("/command/setGlobalUpLimit", {'limit' : limit})
    
def getTorrentDownloadLimit(torrentHash):
    response = qbwebapiPost("/command/getTorrentDlLimit", {'hash' : torrentHash})
    
    return int(response.text)
    
def setTorrentDownloadLimit(torrentHash, limit):
    response = qbwebapiPost("/command/setTorrentDlLimit", {'hash' : torrentHash, 'limit' : limit})
    
def getTorrentUploadLimit(torrentHash):
    response = qbwebapiPost("/command/getTorrentUpLimit", {'hash' : torrentHash})
    
    return int(response.text)
    
def setTorrentUploadLimit(torrentHash, limit):
    response = qbwebapiPost("/command/setTorrentUpLimit", {'hash' : torrentHash, 'limit' : limit})

    
def setPreferences(pref):
    data = json.dumps(pref)
    
    response = qbwebapiPost("/command/setPreferences", {'json' : data})