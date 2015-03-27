import qbwebapi

#Set essential parameters. Use this before anything else
qbwebapi.setParams({'user' : 'admin', 'password' : '1234', 'port' : 8080, 'url' : 'http://192.168.0.12'})

#Add a torrent from a url.
qbwebapi.addTorrent({"http://releases.ubuntu.com/14.10/ubuntu-14.10-desktop-amd64.iso.torrent"})

#Add torrents from several urls
urls = {"http://images.kali.org/kali-linux-1.1.0a-amd64.torrent",
"http://cdimage.debian.org/debian-cd/7.8.0/amd64/bt-cd/debian-7.8.0-amd64-CD-1.iso.torrent"}

qbwebapi.addTorrent(urls)

#Get the torrent lit into a json object
json = getTorrents()

#Prints the name of the first torrent
print(json[0]['name'])

#The hash that represents the torrent. Mandatory for using single torrent functions
hash = json[0]['hash']

#Pause the torrent associated with the hash
pauseTorrent(hash)





