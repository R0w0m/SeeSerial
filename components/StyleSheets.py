
# "purple": ("#CFC8FF", "#9D92E9", "#8072DC", "#6C5DD3"),
# "blue": ("#3F8CFF", "#A0D7E7", "#CCF3FE", "#0049C6"),
# "pink": ("#FF77A3", "#FFC6DB", "#FFBED3", "#FFA2C0"),
# "orange": ("#FFA25F", "#FFE1AA", "#FFDD9D", "#FFCE73"),
# "black": ("#FFFFFF", "#8D8E90", "#494A4D", "#1B1D21"),

class StyleSheets:
    def __init__(self, color):
        # text
        # #1B1D21
        # #808191
        text_colors = {
            "black": "#1B1D21",
            "gray": "#808191",
        }
        colors = {
            # color: [background, button, hover, pressed, logo, text, text_hover, text_pressed]
            "purple": ("#FFF", "#CFC8FF", "#9D92E9", "#8072DC", "#6C5DD3", "#1B1D21", "#808191"),
        #     "purple": {
        #         "background": "#FFF",
        #         "button": "#CFC8FF",
        #         "hover": "#9D92E9",
        #         "pressed": "#8072DC",
        #         "logo": "#6C5DD3",
        #         "text": "#1B1D21",
        #         "text_hover": "#808191",
        #         "text_pressed": "#808191",
        # }
            "blue": ("#FFF", "#3F8CFF", "#A0D7E7", "#CCF3FE", "#0049C6"),
            "pink": ("#FFF", "#FF77A3", "#FFC6DB", "#FFBED3", "#FFA2C0"),
            "orange": ("#FFF", "#FFA25F", "#FFE1AA", "#FFDD9D", "#FFCE73"),
            "black": ("#0F0F0F", "#FFFFFF", "#8D8E90", "#494A4D", "#1B1D21"),
        }
        self.color = colors[color]
        self.styles = {
            "main": f"""
                background-color: {colors[color][0]};
                color: {text_colors["black"]};
                font-size: 16px;
                font-family: 'Roboto', sans-serif;
            """,
            "button": f"""
                QPushButton {{
                    background-color: {colors[color][1]};
                    color: {colors[color][5]};
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 8px 16px;
                    text-align: left;
                }}

                QPushButton:hover {{
                    background-color: {colors[color][2]};
                    color: black;
                }}

                QPushButton:pressed {{
                    background-color: {colors[color][3]};
                    color: white;
                }}
            """,
            "logo": f"""
                QLabel {{
                    background-color: {colors[color][4]};
                    border-radius: 10px;
                    color: white;
                    font-size: 30px;
                    padding: 8px 16px;
                    text-align: center;
                }}
                """,
            "scrollBar": """
                QScrollBar:vertical {
                    border: none;
                    background: transparent;
                    width: 6px;
                    margin: 0;
                    border-radius: 3px;
                }
                QScrollBar::handle:vertical {
                    background: #777777;
                    min-height: 0px;
                    border-radius: 3px;
                }
                QScrollBar::add-line:vertical {
                    border: none;
                    background: none;
                }
                QScrollBar::sub-line:vertical {
                    border: none;
                    background: none;
                }
                QScrollBar::add-page:vertikal, QScrollBar::sub-page:vertical {
                    background: none;
                }

                QScrollBar:vertical:hover {
                    background: #aaaaaa;
                    width: 10px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #181a1b;
                }
                QScrollBar::add-line:vertical:hover {
                    background: #aaaaaa;
                }
                """,
            "widget": """
                    background-color: rgb(255, 255, 255);
                    border-radius: 10px;""",
        }
