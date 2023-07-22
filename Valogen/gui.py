import sys
from PyQt6.QtCore import Qt, QEventLoop, QTimer, QSize, QRect, QThread, pyqtSignal
from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtWidgets import  QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSpacerItem, QSizePolicy
from qfluentwidgets import (InfoBarIcon, InfoBar, setTheme, Theme, InfoBarPosition, SplashScreen, CardWidget, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, Action, PushButton, StateToolTip, ComboBox)
from qframelesswindow import FramelessWindow

from importlib import import_module

class BotThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self, bot_gen):
        QThread.__init__(self)
        self.bot_gen = bot_gen 
    def run(self):
        bot = self.bot_gen()
        username, password, email = bot.login()
        self.signal.emit((username, password, email))

class CredentialCard(CardWidget):
    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton('Copy', self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(83)
        self.iconWidget.setFixedSize(18, 18)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 20, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignmentFlag.AlignRight)

        self.openButton.clicked.connect(self.copy_to_clipboard)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.titleLabel.text())

class Credits(QWidget):
    def __init__(
        self,
        copyright,
        version,
        bg_two,
        text_size,
        text_description_color,
        radius = 8,
        padding = 10
    ):
        super().__init__()

        # PROPERTIES
        self._copyright = copyright
        self._version = version
        self._bg_two = bg_two
        self._text_size = text_size
        self._text_description_color = text_description_color
        self._radius = radius
        self._padding = padding

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0,0,0,0)

        # BG STYLE
        style = f"""
        #bg_frame {{
            border-radius: {self._radius}px;
            background-color: {self._bg_two};
        }}
        .QLabel {{
            color: {self._text_description_color};
            padding-left: {self._padding}px;
            padding-right: {self._padding}px;
        }}
        """

        # BG FRAME
        self.bg_frame = QFrame()
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(style)

        # ADD TO LAYOUT
        self.widget_layout.addWidget(self.bg_frame)

        # ADD BG LAYOUT
        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(0,0,0,0)

        # ADD COPYRIGHT TEXT
        self.copyright_label = QLabel(self._copyright)
        self.copyright_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # ADD VERSION TEXT
        self.version_label = QLabel(self._version)
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # SEPARATOR
        self.separator = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # ADD TO LAYOUT
        self.bg_layout.addWidget(self.copyright_label)
        self.bg_layout.addSpacerItem(self.separator)
        self.bg_layout.addWidget(self.version_label)

class App(FramelessWindow):
    def __init__(self):
        super().__init__()
        setTheme(Theme.DARK)
        self.resize(400, 600)
        self.setWindowTitle('ValoGen+')
        self.setWindowIcon(QIcon('assets/logoVG.png'))
        self.cards = []
        self.thread = None

        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))
        self.show()

        self.createSubInterface()
        self.splashScreen.finish()
        self.showMainSubInterface()

    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(2000, loop.quit)
        loop.exec()

    def showMainSubInterface(self):
        pixmap = QIcon("assets/titleVG.png")
        pixmap = pixmap.pixmap(200, 200)
        imageLabel = QLabel()
        imageLabel.setPixmap(pixmap)
        imageLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout = QVBoxLayout(self)
        self.layout.addSpacing(20)
        self.layout.addWidget(imageLabel)

        self.comboBox = ComboBox(self)
        items = ['Chrome', 'Firefox']
        self.current_bot_gen = self.get_bot_gen(items[0].lower())
        self.comboBox.addItems(items)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentTextChanged.connect(self.handle_browser_change)
        self.layout.addWidget(self.comboBox)

        self.addCard(FluentIcon.MAIL, "", 'email')
        self.addCard(FluentIcon.PEOPLE, "", 'username')
        self.addCard(FluentIcon.ASTERISK, "", 'password')

        self.generate_acc_btn = PushButton('Generate Account', self, FluentIcon.ADD)
        # self.generate_acc_btn.setStyleSheet("background-color: rgb(0,144,255); color: white;")
        self.generate_acc_btn.clicked.connect(self.creator)
        self.stateTooltip = None
        self.layout.addWidget(self.generate_acc_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addSpacing(20)
        # CREDITS
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0,0,0,0)

        self.credits = Credits(
            bg_two = "#444444",
            copyright = "By: Balduzz",
            version = "v.1.0.0",
            text_size = 9,
            text_description_color = "#A0A0A0"
        )

        self.credits_layout.addWidget(self.credits)
        self.layout.addWidget(self.credits_frame)

    def get_bot_gen(self, browser):
        module = import_module(f"src.{browser}")  # dynamically import the module based on the browser string
        return module.RiotGen

    def handle_browser_change(self, browser):
        self.current_bot_gen = self.get_bot_gen(browser.lower())  # update the bot generator when the sel

    def addCard(self, icon, title, content):
        card = CredentialCard(icon, title, content, self)
        self.cards.append(card)  # save a reference to the card
        self.layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignTop)

    def creator(self):
        # Initialize the thread here
        self.thread = BotThread(self.current_bot_gen)
        self.thread.signal.connect(self.update_credential_cards)

        self.stateTooltip = StateToolTip('Generating account', 'Please be patient', self)
        self.stateTooltip.move(self.width() - self.stateTooltip.width() - 20, 30)
        self.stateTooltip.show()
        
        self.thread.start()

    def update_credential_cards(self, data):
        for card, new_title in zip(self.cards, data):
            card.titleLabel.setText(new_title)

        if self.stateTooltip:
            self.stateTooltip.setContent('Account Created 😆')
            self.stateTooltip.setState(True)
            self.stateTooltip = None

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Dark Theme for the framelesswindow
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(palette)

    w = App()
    w.show()
    app.exec()
