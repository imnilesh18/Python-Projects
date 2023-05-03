from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.contents[0].get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
# print(largest_number)
largest_index = article_upvotes.index(largest_number)
# print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(int(article_upvotes[0].split()[0]))

# /robots.txt


# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# name = soup.select_one(selector="#name")
# # print(name)
#
# headings = soup.select(".heading")
# print(headings)
