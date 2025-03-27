import re
import sys


def main():
    print(parse(input("HTML: ")))

# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

def parse(s):
    if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()