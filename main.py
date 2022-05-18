import sys
from take_picture import take_picture1, close_cam
from conversion import conversion1
from build_yml import build_yml1
from recognize import recognize1


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


def do_photo():
    print("开始拍照")
    take_picture1()
    # close_cam()
    print("拍照结束")


def do_train():
    print("开始训练")
    conversion1()
    build_yml1()


def do_discern():
    print("开始识别")
    recognize1()


def do_login():
    print("汪棋")
    print(user_edit.text())
    print(pwd_edit.text())
    if user_edit.text() == "admin" and pwd_edit.text() == "123456":
        print("登录成功")
        user_edit.hide()
        pwd_edit.hide()
        user_label.hide()
        login_btn.hide()
        photo_btn.show()
        train_btn.show()
        discern_btn.show()

    else:
        print("登录失败")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_win = QWidget()
    my_win.setWindowTitle("登录窗口")
    my_win.resize(300, 300)

    user_label = QLabel("user", my_win)

    login_btn = QPushButton("login", my_win)
    login_btn.setGeometry(100, 200, 80, 30)

    login_btn.clicked.connect(do_login)

    # 拍照按钮
    photo_btn = QPushButton("拍照", my_win)
    photo_btn.setGeometry(100, 100, 80, 30)
    photo_btn.clicked.connect(do_photo)
    photo_btn.hide()

    # 创建训练和识别按钮
    train_btn = QPushButton("训练", my_win)
    train_btn.setGeometry(100, 150, 80, 30)
    train_btn.clicked.connect(do_train)
    train_btn.hide()
    # 识别
    discern_btn = QPushButton("识别", my_win)
    discern_btn.setGeometry(100, 200, 80, 30)
    discern_btn.clicked.connect(do_discern)
    discern_btn.hide()

    user_edit = QLineEdit(my_win)
    user_edit.setGeometry(80, 20, 100, 30)

    pwd_edit = QLineEdit(my_win)
    pwd_edit.setGeometry(80, 80, 100, 30)

    pwd_edit.setEchoMode(QLineEdit.Password)

    print("ok")

    my_win.show()
    sys.exit(app.exec_())
