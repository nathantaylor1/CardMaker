# Card Maker for Jungle Defense by BarelyBetas
# Code by Nathan Taylor (nathantaylor.nate@gmail.com)
import PySimpleGUI as gui
from textwrap import wrap
from PIL import Image, ImageFont, ImageDraw

def GenerateCard(name: str, cost: int, body: str):
    # Load Assets:
    card = Image.open('Assets/Card.png')
    adventure_font = ImageFont.truetype('Assets/AdventureFont/Adventure.ttf', 52)
    body_font = ImageFont.truetype('Assets/AdventureFont/Adventure.ttf', 38)

    # Card Picture
    #card_img = Image.open("Assets/Black.png")
    #card_img = card_img.resize((420,310))
    #card.paste(card_img, (60,110))

    # Create New Card:
    editable_card = ImageDraw.Draw(card)

    # Set Card Name:
    editable_card.text((60,45), name, (255, 255, 255), font=adventure_font)

    # Set Card Cost:
    editable_card.text((450,45), cost, (255, 255, 255), font=adventure_font)

    # Card Description:
    offset = 450
    for line in wrap(body, width = 24):
        editable_card.text((74, offset), line, (0, 0, 0), font=body_font)
        offset += adventure_font.getsize(line)[1]

    # Save Result:
    fname = name.replace(" ", "")
    card.save(fname+'.png', "PNG")

if __name__ == "__main__":
    layout = [
        [
            gui.Text("Card Name: "),
            gui.Input(key="-NAME-")
        ],
        [
            gui.Text("Card Cost: "),
            gui.Input(key="-COST-")
        ],
        #[
        #    gui.Text("Card Picture: "),
        #    gui.Input(), 
        #    gui.FileBrowse(key="-IMG-")
        #],
        [
            gui.Text("Card Description: "),
            gui.Input(key="-DESC-")
        ],
        [
            gui.Button("EXIT"),
            gui.Button("GENERATE")
        ]
    ]

    # Create the window
    window = gui.Window("Card Maker", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or presses the EXIT button
        if event == "OK" or event == gui.WIN_CLOSED:
            break
        elif event == "GENERATE":
            card_name = values["-NAME-"]
            card_cost = values["-COST-"]
            card_desc = values["-DESC-"]
            #card_img = values["-IMG-"]
            GenerateCard(card_name, card_cost, card_desc)
            break

    window.close()
