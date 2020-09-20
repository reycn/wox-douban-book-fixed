# encoding=utf8
import requests
import webbrowser
from wox import Wox


class Main(Wox):
    def query(self, query):
        if not query:
            return ""
        api_key = '054022eaeae0b00e0fc068c0c0a2102a'
        r = requests.get('https://api.douban.com/v2/book/search?q=' + query +
                         '&apikey=' + api_key)
        r_json = r.json()
        results = []
        for item in r_json['books']:
            res = {}
            title = item['title']
            score = item['rating']['average']
            year = item['pubdate']
            author = item['author']
            publisher = item['publisher']
            res["Title"] = str(title) + ' ' + str(author[0])
            res["SubTitle"] = "⭐" + str(score) + " " + str(
                publisher) + " " + str(year)
            res["IcoPath"] = "Images\\books.png"
            res["JsonRPCAction"] = {
                "method": "openUrl",
                "parameters": [item['alt']]
            }
            results.append(res)
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Main()
