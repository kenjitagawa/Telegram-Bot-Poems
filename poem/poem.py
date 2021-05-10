import requests
import json

def get_poem():
    url = r'https://poetrydb.org/random'
    response = requests.get(url).json()[0]

    title = response.get('title')
    author = response.get('author')
    lines = " ".join(response.get('lines'))

    formatted_message = f"""Author: {author}
Title: {title}

{lines}
"""
    
    return formatted_message

if __name__ == '__main__':
    get_poem()