# YouTube Downloader

This python script uses selenium and pytube to download multiple YouTube videos
from a specific channel. It starts from most recent, and goes on until it
reaches the specific limit field.

## How to use

1. Clone this repository
2. Install the required packages using `pip install -r requirements.txt`
3. Change the `CHANNEL_URL` and `LIMIT` fields in `main.py`
4. Run the script using `python3 main.py`

The videos will be downloaded in the `videos` folder. The script will also
create a `videos_data.json` file with the video titles, description, link, and
data published.

## Fields to modify

- `CHANNEL_URL`: The URL of the channel you want to download videos from
- `LIMIT`: The number of videos you want to download

Enjoy!