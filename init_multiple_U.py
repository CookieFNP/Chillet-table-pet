import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPoint, QTimer, QRect


print("当前工作目录:", os.getcwd())
# 项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))


class DeskPet(QLabel):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_folders = []  # 用于存储多个文件夹路径
        self.load_image_folders()  # 加载多个文件夹
        self.current_folder_index = 0  # 当前使用的文件夹索引
        self.current_image_index = 0  # 当前文件夹内图片的索引
        self.loadImages()
        self.showImage(self.current_image_index)
        self.dragging = False
        self.click_pos = QPoint()

    def initUI(self):
        # 设置窗口属性
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(100, 100)

    def load_image_folders(self):
        # 筛选出项目根目录下以KUM结尾的文件夹作为图片文件夹
        for folder in os.listdir(project_root):
            folder_path = os.path.join(project_root, folder)
            if os.path.isdir(folder_path) and folder.endswith("KUM"):
                self.image_folders.append(folder_path)

    def loadImages(self):
        # 读取当前文件夹中的所有PNG文件
        self.current_folder = self.image_folders[self.current_folder_index]
        self.images = [f for f in os.listdir(self.current_folder) if f.endswith('.png')]
        self.images.sort()  # 确保文件按名称排序

    def showImage(self, index):
        # 加载并显示指定索引的图片
        image_path = os.path.join(self.current_folder, self.images[index])
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(QRect(0, 0, 200, 200).size(), Qt.KeepAspectRatio)  # 调整图片大小
        self.setPixmap(scaled_pixmap)
        self.resize(scaled_pixmap.size())

    def nextImage(self):
        # 切换到当前文件夹下的下一张图片
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.showImage(self.current_image_index)

    def nextFolder(self):
        # 切换到下一个文件夹
        self.current_folder_index = (self.current_folder_index + 1) % len(self.image_folders)
        self.loadImages()
        self.current_image_index = 0
        self.showImage(self.current_image_index)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.nextFolder()
            self.dragging = True
            self.click_pos = event.globalPos() - self.pos()
        elif event.button() == Qt.LeftButton:
            self.dragging = True
            self.click_pos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.click_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = DeskPet()
    pet.show()

    # 创建定时器，每3000毫秒切换一次图片
    timer = QTimer()
    timer.timeout.connect(pet.nextImage)
    timer.start(30)

    sys.exit(app.exec_())