from src.Fonts import *
from src.HtmlGenerator import *
from src.TemplateSet import *
from src.CardList import *
from src.WebBrowser import *
from src.Daemon import *

import sys

# ---------- PROCESS SYS ARGUMENTS ---------- #
OUTPUT_FOLDER = sys.argv[1]
TEMPLATE_FILE = sys.argv[2]
DATA_FILE = sys.argv[3]
HTML_FILE_NAME = "index"
if len(sys.argv) > 4:
    HTML_FILE_NAME = sys.argv[4]

DEBUG_MODE = False    
SORT = False
if len(sys.argv) > 5:
    for i in range(5, len(sys.argv)):
        if sys.argv[i] == "--debug":
            DEBUG_MODE = True
        elif sys.argv[i] == "--sort" or sys.argv[i] == "--sorted":
            SORT = True
# ------------------------------------------- #

def generate_cards():
    HtmlGenerator.init(HTML_FILE_NAME) 
    TemplateSet.load(TEMPLATE_FILE)
    CardList.load(DATA_FILE)

    cards = CardList.cards.values()

    if SORT:
       cards = sort_cards(cards)

    for card in cards:
        template = TemplateSet.get_template(card.card_type)
        template.write_card(card, DEBUG_MODE)

    HtmlGenerator.end()

    print("Cards Printed >>>", len(cards))    

def sort_cards(cards):
    cards = sorted(cards, key=lambda c: c.card_type)

    by_type = {}
    for card in cards:
        if card.card_type not in by_type:
            by_type[card.card_type] = []
        by_type[card.card_type].append(card)

    sorted_cards = []
    for key in by_type:
        by_type[key] = sorted(by_type[key], key=lambda c: c.card_type)
        sorted_cards.extend(by_type[key])

    return sorted_cards


def process_args():
    global OUTPUT_FOLDER, TEMPLATE_FILE, DATA_FILE, HTML_FILE_NAME
    if not os.path.isabs(TEMPLATE_FILE):
        TEMPLATE_FILE = os.path.normpath(os.path.join(OUTPUT_FOLDER, TEMPLATE_FILE))

    if not os.path.isabs(DATA_FILE):
        DATA_FILE = os.path.normpath(os.path.join(OUTPUT_FOLDER, DATA_FILE))

    if not os.path.isabs(HTML_FILE_NAME):
        HTML_FILE_NAME = os.path.normpath(os.path.join(OUTPUT_FOLDER, HTML_FILE_NAME))


def main():  
    process_args()
    
    Fonts.init(OUTPUT_FOLDER)

    generate_cards()

    Daemon.watch_file(DATA_FILE)
    Daemon.watch_file(TEMPLATE_FILE)
    WebBrowser.init(OUTPUT_FOLDER)
    WebBrowser.open()
    
    while WebBrowser.is_open():
        if Daemon.check():
            try:
                generate_cards()
                WebBrowser.refresh()   
            except Exception as e: print(e)     

        time.sleep(0.5)
   
    Daemon.stop_watching(DATA_FILE)
    Daemon.stop_watching(TEMPLATE_FILE)

# --------------------- ENTRY --------------------- #
    
main()

# ------------------------------------------------- #
