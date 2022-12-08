import requests as req
from bs4 import BeautifulSoup as bs
import webbrowser as wb

print("Nathan Landivar (npl5192)\n")
print("Finding a random wikipedia article..")
while True:
    url = req.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = bs(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"{title} \nDo you want to view it? (Y/N)")
    ans = input("").lower()

    if ans == "y":
        print("Opening page in browser!")
        url = "https://en.wikipedia.org/wiki/%s" % title
        wb.open(url)
        break
    elif ans == "n":
        print("Finding another page..")
        continue
    else:
        print("Invalid input. Closing.")
        break
