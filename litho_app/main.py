import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLabel, QFileDialog, QDoubleSpinBox
)
from litho_engine import generate_lithophane


class LithoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lithophane Generator")
        self.image_path = None

        layout = QVBoxLayout(self)

        self.btn_img = QPushButton("Load Image")
        self.btn_img.clicked.connect(self.load_image)
        layout.addWidget(self.btn_img)

        self.lbl_img = QLabel("No image loaded")
        layout.addWidget(self.lbl_img)

        grid = QGridLayout()
        self.width = self.spin(grid, "Width (mm)", 0, 100)
        self.height = self.spin(grid, "Height (mm)", 1, 60)
        self.min_t = self.spin(grid, "Min Thickness (mm)", 2, 0.8)
        self.max_t = self.spin(grid, "Max Thickness (mm)", 3, 3.2)
        self.base_t = self.spin(grid, "Base Thickness (mm)", 4, 1.0)
        layout.addLayout(grid)

        self.btn_export = QPushButton("Export STL")
        self.btn_export.clicked.connect(self.export)
        layout.addWidget(self.btn_export)

        self.status = QLabel("")
        layout.addWidget(self.status)

    def spin(self, layout, text, row, value):
        lbl = QLabel(text)
        box = QDoubleSpinBox()
        box.setRange(0.1, 1000)
        box.setDecimals(2)
        box.setValue(value)
        layout.addWidget(lbl, row, 0)
        layout.addWidget(box, row, 1)
        return box

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if path:
            self.image_path = path
            self.lbl_img.setText(path.split("/")[-1])

    def export(self):
        if not self.image_path:
            self.status.setText("Load image first")
            return

        mesh = generate_lithophane(
            image_path=self.image_path,
            width_mm=self.width.value(),
            height_mm=self.height.value(),
            min_thickness=self.min_t.value(),
            max_thickness=self.max_t.value(),
            base_thickness=self.base_t.value()
        )

        mesh.export("output.stl")
        self.status.setText("Saved output.stl")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LithoApp()
    win.show()
    sys.exit(app.exec())
