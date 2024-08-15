import re

import html2text
import requests
from bs4 import BeautifulSoup


def sanitize_filename(name):
    # Replace invalid characters with an underscore or other safe character
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def get_program(url: str) -> dict:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        dict: _description_
    """
    # Fetch the web page with data2day programm
    response = requests.get(url)

    program = {}
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Extracting all links
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            text = link.get_text()
            if "html" in str(href) and "»" not in text and "TBA" not in text:
                # print(f'Text: {text}, URL: {href}')
                program[text] = f"https://www.data2day.de/{href}"
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return program


def get_formatted_text_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        converter = html2text.HTML2Text()
        converter.ignore_links = False  # Set to True if you want to ignore links
        formatted_text = converter.handle(str(soup))
        return formatted_text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


def save_text(text: str, name: str) -> None:
    """_summary_

    Args:
        text (str): _description_
        name (str): _description_
    """
    # sanitize file name for windows
    name = sanitize_filename(name)

    # save as markdown
    with open(f'data/{name.replace(" ", "_")}.md', "w", encoding="utf-8") as md_file:
        md_file.write(text)

    # save as plain text
    # with open(
    #     f'data/text/{name.replace(" ", "_")}.txt', "w", encoding="utf-8"
    # ) as txt_file:
    #     txt_file.write(text)


def extract_text(url: str, name: str) -> None:
    """_summary_

    Args:
        url (str): _description_
        name (str): _description_
    """
    # extract text from url
    formatted_text = get_formatted_text_from_website(url)

    if formatted_text:
        text = formatted_text.split("\n")
        # join to one string and remove empty strings
        text = list(filter(None, text))

        start, end = None, None
        for n, line in enumerate(text):
            if line.startswith(f"# {name[:20]}"):
                start = n
            elif line.startswith("## data2day-Newsletter"):
                end = n
            if start and end:
                break

        contiguous_text = "\n".join(text[start:end])

        # save as .md and .txt
        save_text(contiguous_text, name)
        print(
            f'saved content of page {url} as {name.replace(" ", "_")}.md and {name.replace(" ", "_")}.txt'
        )
        print()


# url to data2day page with program (= links to workshops and talks)
url = "https://www.data2day.de/programm.php"

# extract links to workshops and talks
program = get_program(url)

# extract abstracts + speaker (and save them in text and markdown files)
for name_value in list(program.keys()):
    name = name_value
    url = program[name]
    extract_text(url, name)
