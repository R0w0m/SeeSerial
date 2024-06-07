
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
        text_color = {
            "black": "#1B1D21",
            "gray": "#808191",
        }
        themes = {
            # color: [background, button, hover, pressed, primary, text, text_hover, text_pressed]
            "purple": ("#FFF", "#CFC8FF", "#9D92E9", "#8072DC", "#6C5DD3", "#1B1D21", "#808191"),
            "blue": ("#FFF", "#3F8CFF", "#A0D7E7", "#CCF3FE", "#0049C6", "#1B1D21", "#808191"),
            "pink": ("#FFF", "#FF77A3", "#FFC6DB", "#FFBED3", "#FFA2C0", "#1B1D21", "#808191"),
            "orange": ("#FFF", "#FFA25F", "#FFE1AA", "#FFDD9D", "#FFCE73", "#1B1D21", "#808191"),
            "black": ("#202222", "#8D8E90", "#FFFFFF", "#494A4D", "#1B1D21", "#808191", "#8D8E90"),
        }
        self.theme = themes[color]
        self.styles = {
            "main": f"""
                background-color: {self.theme[0]};
                color: {self.theme[5]};
                font-size: 16px;
                font-family: 'Roboto', sans-serif;
            """,
            # text align center
            "button": f"""
                QPushButton {{
                    background-color: {self.theme[0]};
                    color: {self.theme[6]};
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 8px 16px;
                    text-align: center;
                }}

                QPushButton:hover {{
                    background-color: {self.theme[2]};
                    color: {self.theme[5]};
                }}

                QPushButton:pressed {{
                    background-color: {self.theme[3]};
                    color: {self.theme[0]};
                }}
            """,
            "accent_button": f"""
                QPushButton {{
                    background-color: {self.theme[1]};
                    color: {self.theme[5]};
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 8px 16px;
                    text-align: left;
                }}

                QPushButton:hover {{
                    background-color: {self.theme[2]};
                    color: {self.theme[6]};
                }}

                QPushButton:pressed {{
                    background-color: {self.theme[3]};
                    color: {self.theme[0]};
                }}
            """,

            "logo": f"""
                QLabel {{
                    background-color: {self.theme[4]};
                    border-radius: 10px;
                    color: white;
                    font-size: 30px;
                    padding: 8px 16px;
                    text-align: center;
                }}
                """,
            # border none for scrollarea
            "scrollBar": f"""
                QScrollArea {{
                    border: none;
                    background-color: {self.theme[0]};
                }}
                QScrollBar:vertical {{
                    border: none;
                    background: transparent;
                    width: 6px;
                    margin: 0;
                    border-radius: 3px;
                }}
                QScrollBar::handle:vertical {{
                    background: #777777;
                    min-height: 0px;
                    border-radius: 3px;
                }}
                QScrollBar::add-line:vertical {{
                    border: none;
                    background: none;
                }}
                QScrollBar::sub-line:vertical {{
                    border: none;
                    background: none;
                }}
                QScrollBar::add-page:vertikal, QScrollBar::sub-page:vertical {{
                    background: none;
                }}

                QScrollBar:vertical:hover {{
                    background: #aaaaaa;
                    width: 10px;
                }}
                QScrollBar::handle:vertical:hover {{
                    background: #181a1b;
                }}
                QScrollBar::add-line:vertical:hover {{
                    background: #aaaaaa;
                }}
                """,
            "widget": """
                    background-color: rgb(255, 255, 255);
                    border-radius: 10px;""",
            "line": f"""
                background-color: #AAAAAA;
                border: none;
                width: 1px;
            """,
            "label": f"""
                color: {self.theme[5]};
                font-size: 16px;
                font-family: 'Roboto', sans-serif;
            """,
            "header": f"""
                color: {self.theme[5]};
                font-size: 24px;
                font-family: 'Roboto', sans-serif;
            """,
            "line_edit": f"""
                background-color: {self.theme[0]};
                color: {self.theme[5]};
                border: 1px solid {self.theme[5]};
                border-radius: 10px;
                font-size: 16px;
                padding: 8px 16px;
            """,
            "episode_ui": f"""
                background-color: {self.theme[1]};
                border-radius: 10px;
            """,
            "text_edit": f"""
                background-color: {self.theme[0]};
                color: {self.theme[5]};
                border: 1px solid {self.theme[5]};
                border-radius: 10px;
                font-size: 16px;
                padding: 8px 16px;
            """,
            "combo_box": f"""
                QComboBox {{
                    background-color: {self.theme[0]};
                    color: {self.theme[5]};
                    border: 1px solid {self.theme[5]};
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 8px 16px;
                }}

                QComboBox::drop-down {{
                    border: none;
                }}

                QComboBox::down-arrow {{
                    image: url(./assets/arrow_down.png);
                }}
            """,
            "check_box": f"""
                QCheckBox {{
                    background-color: {self.theme[6]};
                    border-radius: 15px;
                    padding: 5px;
                }}
                QCheckBox::indicator {{
                    width: 20px;
                    height: 20px;
                    border-radius: 10px;
                    background-color: white;
                }}
                QCheckBox::indicator:checked {{
                    margin-left: 30px;
                }}
                QCheckBox::checked {{
                    background-color: {self.theme[1]};
                }}
            """,
            "contents": f"""
                background-color: {self.theme[0]};
            """,
            "stacked_widget": f"""
                background-color: {self.theme[0]};
            """,
        }

    def get_color(self):
        return self.self.theme
