# Card Maker for Jungle Defense by BarelyBetas
# Code by Nathan Taylor (nathantaylor.nate@gmail.com)
from fileinput import filename
from textwrap import wrap
from PIL import Image, ImageFont, ImageDraw

def SetName():
    editable_card.text((60,45), name, (255, 255, 255), font=adventure_font) # card name

def SetActionPointCost():
    editable_card.text((450,45), cost, (255, 255, 255), font=adventure_font)

#def SetPicture():
    #editable_card.

def SetDescription():
    offset = 450
    for line in wrap(body, width = 24):
        editable_card.text((74, offset), line, (0, 0, 0), font=body_font)
        offset += adventure_font.getsize(line)[1]

if __name__ == "__main__":
    name: str = input("Enter Card Name: ")
    cost: int = input("Enter Card Cost: ")
    #img : str = input("Enter Location of Card Picture: ")
    body: str = input("Enter Card DEscription: ")

    # Load Assets:
    card = Image.open('Assets/Card.png')
    adventure_font = ImageFont.truetype('Assets/AdventureFont/Adventure.ttf', 52)
    body_font = ImageFont.truetype('Assets/AdventureFont/Adventure.ttf', 38)

    # Create New Card:
    editable_card = ImageDraw.Draw(card)

    # Edit Card:
    SetName()
    SetActionPointCost()
    SetDescription()

    # Save Result:
    filename = name.replace(" ", "")
    card.save(filename + '.png')

