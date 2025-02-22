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
        #self.alternate_image_folder = 'yunKUM'  # 另一个文件夹路径
        self.alternate_image_folder = os.path.join(project_root, 'yunKUM')
        self.loadImages()
        self.current_index = 0
        self.showImage(self.current_index)
        self.dragging = False
        self.click_pos = QPoint()
        self.is_alternate = False  # 标记是否使用另一个文件夹

    def initUI(self):
        # 设置窗口属性
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(100, 100)

    def loadImages(self):
        # 读取文件夹中的所有PNG文件
        # self.image_folder = 'KUM'
        self.image_folder = os.path.join(project_root, 'KUM')
        self.images = [f for f in os.listdir(self.image_folder) if f.endswith('.png')]
        self.images.sort()  # 确保文件按名称排序

        # 读取另一个文件夹中的所有PNG文件
        self.alternate_images = [f for f in os.listdir(self.alternate_image_folder) if f.endswith('.png')]
        self.alternate_images.sort()  # 确保文件按名称排序

    def showImage(self, index, is_alternate=False):
        # 加载并显示指定索引的图片
        if is_alternate:
            image_path = os.path.join(self.alternate_image_folder, self.alternate_images[index])
        else:
            image_path = os.path.join(self.image_folder, self.images[index])

        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(QRect(0, 0, 200, 200).size(), Qt.KeepAspectRatio)  # 调整图片大小
        self.setPixmap(scaled_pixmap)
        self.resize(scaled_pixmap.size())

    def nextImage(self):
        # 切换到下一张图片
        if self.is_alternate:
            self.current_index = (self.current_index + 1) % len(self.alternate_images)
            self.showImage(self.current_index, True)
        else:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.showImage(self.current_index, False)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.is_alternate:
                self.is_alternate = False
                self.current_index = 0
                self.showImage(self.current_index, False)
            else:
                self.is_alternate = True
                self.current_index = 0
                self.showImage(self.current_index, True)
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