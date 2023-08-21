
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
