from PyQt5.QtWidgets import QComboBox, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel

from src.base.dao import DAO
from src.base.screen import BaseScreen
from src.cart.models import Cart


class CartScreen(BaseScreen):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

        self.cart_dao = DAO(
            engine=engine,
            model=Cart,
        )

        # Форма добавления лекарства
        self.medicine_combo = QComboBox()
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_to_cart)

        add_layout = QVBoxLayout()
        add_layout.addWidget(QLabel("Выберите лекарство для добавления:"))
        add_layout.addWidget(self.medicine_combo)
        add_layout.addWidget(self.add_button)

        # Форма удаления лекарства
        self.remove_combo = QComboBox()
        self.remove_button = QPushButton("Удалить")
        self.remove_button.clicked.connect(self.remove_from_cart)

        remove_layout = QVBoxLayout()
        remove_layout.addWidget(QLabel("Выберите лекарство для удаления:"))
        remove_layout.addWidget(self.remove_combo)
        remove_layout.addWidget(self.remove_button)

        # Форма расчета стоимости
        self.total_price_field = QLineEdit()
        self.total_price_field.setReadOnly(True)
        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate_total)

        calc_layout = QVBoxLayout()
        calc_layout.addWidget(QLabel("Общая стоимость:"))
        calc_layout.addWidget(self.total_price_field)
        calc_layout.addWidget(self.calculate_button)

        # Таблица корзины
        self.cart_table = QTableWidget()
        self.cart_table.setColumnCount(5)
        self.cart_table.setHorizontalHeaderLabels(["ID", "Name", "Price", "Category", "Manufacturer"])

        self.layout.addLayout(add_layout)
        self.layout.addLayout(remove_layout)
        self.layout.addLayout(calc_layout)
        self.layout.addWidget(self.cart_table)

        self.on_tab_selected()

    def on_tab_selected(self):
        self.load_cart()

    def load_cart(self):
        cart = self.get_cart()
        self.cart_table.setRowCount(len(cart.medicines))
        for row_idx, medicine in enumerate(cart.medicines):
            self.cart_table.setItem(row_idx, 0, QTableWidgetItem(str(medicine.id)))
            self.cart_table.setItem(row_idx, 1, QTableWidgetItem(medicine.name))
            self.cart_table.setItem(row_idx, 2, QTableWidgetItem(str(medicine.price)))
            self.cart_table.setItem(row_idx, 3, QTableWidgetItem(medicine.category.name if medicine.category else ""))
            self.cart_table.setItem(row_idx, 4, QTableWidgetItem(medicine.manufacturer.name if medicine.manufacturer else ""))
        return

    def add_to_cart(self):
        pass

    def remove_from_cart(self):
        pass

    def calculate_total(self):
        pass
