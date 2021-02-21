from pyrogram import Client, filters
import re
import requests
from bs4 import BeautifulSoup


@Client.on_message(filters.regex(r"(https?:\/\/(?:www\.)?instagram\.com\/p\/([^/?#&]+)).*"))
def dl_post(c, m):
    print(m.text)
    url = m.text
    resp = requests.get("https://downloadgram.com")
    soup = BeautifulSoup(resp.text, 'html.parser')

    build_id = soup.find_all("input")[2]['value']
    build_key = soup.find_all("input")[3]['value']

    # url = "https://www.instagram.com/p/CLW31iuLXOz/?utm_source=ig_web_copy_link"
    data = {
        'build_id': build_id,
        'build_key': build_key,
        "url": url,
    }
    hed = {
        "user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}

    urls = requests.post(
        "https://downloadgram.com/process.php", data=data, headers=hed)
    # print(urls.content)
    soup = BeautifulSoup(urls.text, 'html.parser')
    link_dl = soup.a['href']
    m.reply_video(link_dl)
