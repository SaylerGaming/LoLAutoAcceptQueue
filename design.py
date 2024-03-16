################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 294)
        MainWindow.setMinimumSize(QSize(430, 160))
        icon = QIcon()
        icon.addFile(u":/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_write_bot = QPushButton(self.centralwidget)
        self.btn_write_bot.setObjectName(u"btn_write_bot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_write_bot.sizePolicy().hasHeightForWidth())
        self.btn_write_bot.setSizePolicy(sizePolicy)
        self.btn_write_bot.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_write_bot)

        self.btn_set_id = QPushButton(self.centralwidget)
        self.btn_set_id.setObjectName(u"btn_set_id")
        sizePolicy.setHeightForWidth(self.btn_set_id.sizePolicy().hasHeightForWidth())
        self.btn_set_id.setSizePolicy(sizePolicy)
        self.btn_set_id.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_set_id)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_chat_id = QLabel(self.centralwidget)
        self.lbl_chat_id.setObjectName(u"lbl_chat_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_chat_id.sizePolicy().hasHeightForWidth())
        self.lbl_chat_id.setSizePolicy(sizePolicy1)
        self.lbl_chat_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_chat_id)

        self.le_chat_id = QLineEdit(self.centralwidget)
        self.le_chat_id.setObjectName(u"le_chat_id")
        self.le_chat_id.setCursor(QCursor(Qt.IBeamCursor))
        self.le_chat_id.setReadOnly(False)

        self.verticalLayout_6.addWidget(self.le_chat_id)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.le_accept_queue_sensitivity = QLineEdit(self.centralwidget)
        self.le_accept_queue_sensitivity.setObjectName(u"le_accept_queue_sensitivity")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_accept_queue_sensitivity.sizePolicy().hasHeightForWidth())
        self.le_accept_queue_sensitivity.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.le_accept_queue_sensitivity)

        self.lbl_accept_queue_sensitivity = QLabel(self.centralwidget)
        self.lbl_accept_queue_sensitivity.setObjectName(u"lbl_accept_queue_sensitivity")
        sizePolicy2.setHeightForWidth(self.lbl_accept_queue_sensitivity.sizePolicy().hasHeightForWidth())
        self.lbl_accept_queue_sensitivity.setSizePolicy(sizePolicy2)
        self.lbl_accept_queue_sensitivity.setMinimumSize(QSize(0, 50))
        self.lbl_accept_queue_sensitivity.setScaledContents(False)
        self.lbl_accept_queue_sensitivity.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_accept_queue_sensitivity)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.le_in_queue_sensitivity = QLineEdit(self.centralwidget)
        self.le_in_queue_sensitivity.setObjectName(u"le_in_queue_sensitivity")
        sizePolicy2.setHeightForWidth(self.le_in_queue_sensitivity.sizePolicy().hasHeightForWidth())
        self.le_in_queue_sensitivity.setSizePolicy(sizePolicy2)
        self.le_in_queue_sensitivity.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.le_in_queue_sensitivity)

        self.lbl_in_queue_sensitivity = QLabel(self.centralwidget)
        self.lbl_in_queue_sensitivity.setObjectName(u"lbl_in_queue_sensitivity")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_in_queue_sensitivity.sizePolicy().hasHeightForWidth())
        self.lbl_in_queue_sensitivity.setSizePolicy(sizePolicy3)
        self.lbl_in_queue_sensitivity.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_in_queue_sensitivity)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.btn_find_game = QPushButton(self.centralwidget)
        self.btn_find_game.setObjectName(u"btn_find_game")
        self.btn_find_game.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_find_game.sizePolicy().hasHeightForWidth())
        self.btn_find_game.setSizePolicy(sizePolicy4)
        self.btn_find_game.setMinimumSize(QSize(0, 50))
        self.btn_find_game.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_find_game)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.status_layout = QHBoxLayout()
        self.status_layout.setObjectName(u"status_layout")
        self.lbl_status_static = QLabel(self.centralwidget)
        self.lbl_status_static.setObjectName(u"lbl_status_static")

        self.status_layout.addWidget(self.lbl_status_static)

        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.status_layout.addWidget(self.lbl_status)


        self.gridLayout.addLayout(self.status_layout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LoL Match Notifier", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u0441\u0430\u0442\u044c \u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u043e\u0439 \u0438\u0433\u0440\u0435?", None))
        self.btn_write_bot.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0431\u043e\u0442\u0443", None))
        self.btn_set_id.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.lbl_chat_id.setText(QCoreApplication.translate("MainWindow", u"Chat ID", None))
        self.lbl_accept_queue_sensitivity.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043a\u043b\u0438\u043a\u0430 \u043f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.lbl_in_queue_sensitivity.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043a\u043d\u043e\u043a\u0438 \"\u0432 \u043e\u0447\u0435\u0440\u0435\u0434\u0438\"", None))
        self.btn_find_game.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0438\u0433\u0440\u0443", None))
#if QT_CONFIG(shortcut)
        self.btn_find_game.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_status_static.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0435 \u0432 \u043f\u043e\u0438\u0441\u043a\u0435", None))
    # retranslateUi

