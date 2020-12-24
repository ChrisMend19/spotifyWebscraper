from bs4 import BeautifulSoup
import json

# Open up source code and pipe to bs4
with open("sourcecode2.html", "r") as f:
    soup = BeautifulSoup(f, features = "html.parser")

# Find the h2 tag that has all the albums heading
albumTag = soup.find("h2", string = "Albums")

# Find the parent section of the h2 tag
albumSection = albumTag.find_parent("section")

# Find all list items within the section tag
albums = albumSection.findAll("li")

# Iterate through list items and extract data
#album =  albums[0]

allAlbumDetails = []

for album in albums:
    aTag = album.find("a")
    albumLink = aTag["href"]
    albumName = aTag["alt"]

    albumImageDiv = aTag.find("div", {"class": "grid-item-image"})
    albumImage = albumImageDiv["data-src"]

    #print(albumLink, albumName, albumImage, sep = "\n")

    albumDetails = {
        "name": albumName,
        "link": albumLink,
        "cover": albumImage 
    }

    allAlbumDetails.append(albumDetails)

#print(allAlbumDetails)
# Write the extracted data to data file

with open("albums.json", "w") as a:
    json.dump(allAlbumDetails, a)