import json

import pytube
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Change these variables only
CHANNEL_URL = "https://www.youtube.com/@YouTube/videos"  # Url of channel on the videos tab
LIMIT = 5  # Number of videos to download from the channel

# Max limit is around 30, however many videos it loads at the start
# TODO: Make it so it scrolls down and load more videos

# Sets options for webdriver
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# Opens URL
driver = webdriver.Chrome(options=options,
                          service=Service(ChromeDriverManager().install()))
driver.get(CHANNEL_URL)
driver.execute_script("window.scrollTo(0, 10000);")

# Finds video elements
videos = driver.find_elements(By.XPATH, "//a[@id='video-title-link']")
output = {}

# Loops through videos
for i, video in enumerate(videos):
    if i >= LIMIT:
        break

    try:
        # Obtains the video link
        link = video.get_attribute('href')

        youtube = pytube.YouTube(link)
        video = youtube.streams.get_highest_resolution()

        # Gets data about the video
        title = youtube.title
        description = youtube.description
        date = youtube.publish_date.strftime("%m/%d/%Y, %H:%M:%S")

        output[title] = {'link': link, 'description': description, 'date': date}

        # Downloads the video
        video.download('./videos')

        print(f"Downloaded {title}")
    except:
        print(video.text)

with open('output.json', 'w') as outputFile:
    outputFile.write(json.dumps(output))
