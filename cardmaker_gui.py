# Card Maker for Jungle Defense by BarelyBetas
# Code by Nathan Taylor (nathantaylor.nate@gmail.com)
import PySimpleGUI as gui
import cardmaker

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
            cardmaker.GenerateCard(card_name, card_cost, card_desc)
            break

    window.close()
