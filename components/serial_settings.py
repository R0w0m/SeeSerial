def deletePrev_clicked(ui):
    # set image to default and write it to self.prev_set
    ui.prevImage.setStyleSheet(
        " \
        image: url(previwes/default.png); \
        border-radius: 10%; \
        background-color: rgba(0, 0, 0, 0); \
        margin: 0 0 5 0; \
        "
    )
    ui.prevImage.setScaledContents(True)
    ui.prevImage.show()
    ui.prevImage.setMinimumSize(QSize(130, 200))
    prev_set = None
