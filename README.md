# Bhagavat Gita From Web Scraping

Web Scraping and retrieving different chapters and verse of the Holy Bhagvat Gita.

### Why?
I was bored and wanted to read The Bhagavad Gita.

## Usage

### Install Python 3.6+.

*Go to python [Download Page](https://www.python.org/downloads/ "Go to python download page to download the latest version of python.").*

### 1. Install requirements

        pip3 install -r requirements.txt

>*PIP is a cross-platform package manager for installing and managing Python packages (which can be found in the Python Package Index)*

The above command will install following pacakages.
- BeautifulSoup4
- Requests

### 2. Run `main.py` and follow along

    python3 main.py

## Feature List

- You could choose among different options:
    + Retrieve: Everything - All 700 verses
    + Retrieve: A single chapter - All verses from selected chapter
    + Retrieve: Specific verse from a specific chapter
    + Retrieve and display a random quote & more..
- You could choose to save output file in:
    - Markdown (.md) format (Recommended)
    - Or text (.txt) format
- CTRL + C (^C) will terminate and abort the program in any given time
- And more..

## What's New

- Re-wrote all code from scratch (made more readable and understandable code then before).
- Moved all the functions to separate file *(myfunctions.py)*.
- Menu now is cleaner and has more options.
- Should work in Linux and OS X as well *(Not Tested)*.
- Your won't ever see an traceback.

## Code in Action *Screenshots*

#### Code in Action

<!-- Add a gif of code in action HERE-->
![](media/code-in-action-pic.png "Screenshot.")

#### Sample output file in Markdown file format

![](media/markdown-less.png "Screenshot of output file in markdown format.")

![](media/markdown-more.png "Screenshot of output file in markdown format.")

#### Sample output file in Text file format

![](media/text-less.png "Screenshot of output file in text format.")

![](media/text-more.png "Screenshot of output file in text format.")

## What's Coming
- [ ] Add Readme file
- [ ] Retrieve and download Original verse audio

---
\# The End.
