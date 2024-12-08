from PyQt5.QtWidgets import QMainWindow, QTabWidget
from src.medicine.screen import MedicineScreen
from src.cart.screen import CartScreen
from src.category.screen import MedicineCategoryScreen
from src.manufacturer.screen import ManufacturerScreen
from src.buyer.screen import BuyerScreen

class MainWindow(QMainWindow):
    def __init__(self, db_session):
        super().__init__()
        self.setWindowTitle("Медицинское приложение")

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(MedicineScreen(db_session), "Лекарства")
        self.tabs.addTab(CartScreen(db_session), "Корзина")
        self.tabs.addTab(MedicineCategoryScreen(db_session), "Категории")
        self.tabs.addTab(ManufacturerScreen(db_session), "Производители")
        self.tabs.addTab(BuyerScreen(db_session), "Покупатели")
