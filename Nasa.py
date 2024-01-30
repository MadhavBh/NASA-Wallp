from fileinput import filename
from urllib import response 
import requests
import wget
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import ctypes   

nasa_api = "<YOUR API KEY>"
    
def downloadAPOD(apod_response):
    url = apod_response['url']
    response = requests.get(url)
    print(apod_response['explanation'])
    res = response.status_code
    if apod_response['media_type'] == 'image':
        if res == 200:
            filename = url.split("/")[-1]
            wget.download(url, "C:\\Users\\hp\\Pictures\\Saved Pictures")
            print("file downloaded")
            TempDisplay()
            Upd = input(" do you want to update your wallpaper?(Y/N): ")
            if Upd == "Y" or Upd =="y" or Upd =="yes" or Upd == "Yes" or Upd =="YES":
                setwp()
            else:
                print("okay aborting...")
                pass
        else:
            print("Download failed, the site is down ( maybe... idk everything )")
    else:
        print("The Astronomy Photo Of the Day is not a photo, whatchu upto NASA? anyways I didn't download the video, we'll try again tomorrow")

def TempDisplay():
    filename = getAPOD()['url'].split("/")[-1]
    wallp = mpimg.imread("""C:\\Users\\hp\\Pictures\\Saved Pictures\\{filename}""".format(filename = filename))
    wallpplot = plt.imshow(wallp)
    plt.show()

def getAPOD():
    APOD_url = "https://api.nasa.gov/planetary/apod"
    date = datetime.datetime.date(datetime.datetime.now())
    params = {
        'api_key' : nasa_api,
        'date': date,
        'hd' : 'True'
            }
    response = requests.get(APOD_url, params=params).json()
    return response

def setwp():
    filename = getAPOD()['url'].split("/")[-1]
    #PyWallpaper.change_wallpaper("""C:\\Users\\hp\\Pictures\\Saved Pictures\\{filename}""".format(filename = filename))
    ctypes.windll.user32.SystemParametersInfoW(20, 0,"""C:\\Users\\hp\\Pictures\\Saved Pictures\\{filename}""".format(filename = filename) , 0)
    print("wallpaper updated")



if __name__ == "__main__":
    downloadAPOD(getAPOD())