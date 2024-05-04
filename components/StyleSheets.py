style = {
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
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
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


class StyleSheets:
    def __init__(self, color):
        self.color = colors[color]
        # text
        # #1B1D21
        # #808191
        text_colors = {
            "black": "#1B1D21",
            "gray": "#808191",
        }
        colors = {
            "purple": {1: "#CFC8FF", 2: "#9D92E9", 3: "#8072DC", 4: "#6C5DD3"},
            "blue": {1: "#3F8CFF", 2: "#A0D7E7", 3: "#CCF3FE", 4: "#0049C6"},
            "pink": {1: "#FF77A3", 2: "#FFC6DB", 3: "#FFBED3", 4: "#FFA2C0"},
            "orange": {1: "#FFA25F", 2: "#FFE1AA", 3: "#FFDD9D", 4: "#FFCE73"},
            "black": {1: "#FFFFFF", 2: "#8D8E90", 3: "#494A4D", 4: "#1B1D21"},
        }
        self.styles = {
            "button": f"""
                QPushButton {{
                    background-color: {colors[color][1]};
                    color: {colors[color][3]};
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
        }
