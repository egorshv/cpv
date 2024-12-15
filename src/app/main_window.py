from PyQt5.QtWidgets import QMainWindow, QTabWidget
from src.medicine.tab import MedicineTab
from src.cart.tab import CartTab
from src.category.tab import MedicineCategoryTab
from src.manufacturer.tab import ManufacturerTab
from src.buyer.tab import BuyerTab

class MainWindow(QMainWindow):
    def __init__(self, engine):
        super().__init__()
        self.setWindowTitle("Медицинское приложение")

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(MedicineTab(engine), "Лекарства")
        self.tabs.addTab(CartTab(engine), "Корзина")
        self.tabs.addTab(MedicineCategoryTab(engine), "Категории")
        self.tabs.addTab(ManufacturerTab(engine), "Производители")
        self.tabs.addTab(BuyerTab(engine), "Покупатели")
        self.tabs.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        current_widget = self.tabs.widget(index)
        if hasattr(current_widget, "on_tab_selected"):
            current_widget.on_tab_selected()
