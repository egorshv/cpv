from PyQt5.QtWidgets import QMainWindow, QTabWidget
from src.medicine.screen import MedicineScreen
from src.cart.screen import CartScreen
from src.category.screen import MedicineCategoryScreen
from src.manufacturer.screen import ManufacturerScreen
from src.buyer.screen import BuyerScreen

class MainWindow(QMainWindow):
    def __init__(self, engine):
        super().__init__()
        self.setWindowTitle("Медицинское приложение")

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(MedicineScreen(engine), "Лекарства")
        self.tabs.addTab(CartScreen(engine), "Корзина")
        self.tabs.addTab(MedicineCategoryScreen(engine), "Категории")
        self.tabs.addTab(ManufacturerScreen(engine), "Производители")
        self.tabs.addTab(BuyerScreen(engine), "Покупатели")
        self.tabs.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        current_widget = self.tabs.widget(index)
        if hasattr(current_widget, "on_tab_selected"):
            current_widget.on_tab_selected()
