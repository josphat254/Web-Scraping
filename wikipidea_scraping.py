#importing libraries
from bs4 import BeautifulSoup
import requests
import lxml

# Function to Get and parse html content from a Wikipedia page
url = 'https://en.wikipedia.org/wiki/Dedan_Kimathi'
def get_html_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

html_content = get_html_content(url)
#print(html_content)

# Function to Extract article title
def get_article_title(soup):
    article_title = soup.find('h1', class_='firstHeading mw-first-heading').span.text
    return article_title

print(get_article_title(html_content))


# Function to Extract article text for each paragraph with their respective headings. Map those headings to their respective paragraphs in the dictionary.
paragraph_dict = {}
def get_article_paragraphs(_html_content):

  #finding all divs that contain paragraphs
  paragraph_divs = _html_content.find_all('div', class_='mw-heading mw-heading2')
  for div in paragraph_divs:
    #accessing the headings representing each paragraph

    heading = div.find('h2')
    for heading_text in heading:
      #accessing the paragraph text below each heading

      paragraph_text = heading_text.find_next('p')
      if paragraph_text:
        #storing the results in a dictionary

        paragraph_dict[heading.text] = paragraph_text.text[:15]
        #print(paragraph_text.text)

get_article_paragraphs(html_content)
print(paragraph_dict)


#Write a function to collect every link that redirects to another Wikipedia page
def get_redirect_links(_html_content):
  links = _html_content.find_all('a')
  for link in links:
    print(link.text)

get_redirect_links(html_content)