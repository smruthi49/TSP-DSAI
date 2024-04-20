# have beautifulsoup4 and requests installed.
# pip install beautifulsoup4
# pip install requests7

from PIL import Image
import requests as req
import os, bs4

URL = "https://xkcd.com/"

#a directory to store the images
os.makedirs('xkcd', exist_ok = True)
i = 1

while True:
    url = URL + str(i)
    print(f"Downloading the comic {i}...")
    
    if not req.get(url):
        print("No more comics to download!")
        break

    #requesting the url
    res = req.get(url)

    #storing the HTML page found in URL
    soup = bs4.BeautifulSoup(res.text)

    comicElement = soup.select('#comic img')

    #get the source of the image and make it as a URL
    comicURL = 'https:' + comicElement[0].get('src')

    res = req.get(comicURL)
    print(os.path.basename(comicURL))

    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')

    for chunk in res.iter_content(10):
        imageFile.write(chunk)

    #close the binary image file
    imageFile.close()
    print("Downloaded the comic successfully!")
    
    i += 1
    

images = [Image.open('xkcd/'+ im).convert('RGB') for im in os.listdir('xkcd')]

#save the images as PDF
pdf_path = "xkcd_comics.pdf"

images[0].save(pdf_path, save_all = True, append_images = images[1:])