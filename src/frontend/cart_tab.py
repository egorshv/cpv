from PyQt5.QtWidgets import QComboBox, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel

from src.backend.dao import DAO
from src.frontend.base_tab import BaseTab
from src.backend.models.cart import Cart
from src.backend.facades.cart import CartFacade
from src.backend.models.medicine import Medicine


class CartTab(BaseTab):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

        self.cart_dao = DAO(
            engine=engine,
            model=Cart,
        )
        self.medicine_dao = DAO(
            engine=engine,
            model=Medicine,
        )

        self.cart = self.get_cart()
        self.cart_service = CartFacade(self.cart, self.cart_dao)

        # Форма добавления лекарства
        self.medicine_combo = QComboBox()
        self.add_button = QPushButton("Добавить")
        # self.add_quantity_combo = QComboBox()
        self.add_button.clicked.connect(self.add_to_cart)

        add_layout = QVBoxLayout()
        add_layout.addWidget(QLabel("Выберите лекарство для добавления:"))
        add_layout.addWidget(self.medicine_combo)
        # add_layout.addWidget(QLabel('Выберете количество:'))
        # add_layout.addWidget(self.add_quantity_combo)
        add_layout.addWidget(self.add_button)

        # Форма удаления лекарства
        self.remove_combo = QComboBox()
        # self.remove_quantity_combo = QComboBox()
        self.remove_button = QPushButton("Удалить")
        self.remove_button.clicked.connect(self.remove_from_cart)

        remove_layout = QVBoxLayout()
        remove_layout.addWidget(QLabel("Выберите лекарство для удаления:"))
        remove_layout.addWidget(self.remove_combo)
        # remove_layout.addWidget(QLabel("Выберете количество для удаления:"))
        # remove_layout.addWidget(self.remove_quantity_combo)
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

        # self.medicine_combo.currentIndexChanged.connect(self.load_add_quantity)
        # self.remove_combo.currentIndexChanged.connect(self.load_remove_quantity)
        self.on_tab_selected()

    def on_tab_selected(self):
        self.load_cart()
        self.load_medicines(self.remove_combo)
        self.load_medicines(self.medicine_combo)

    def load_add_quantity(self):
        medicine_name = self.medicine_combo.currentText()
        medicine = self.medicine_dao.get(name=medicine_name)

        self.add_quantity_combo.clear()
        self.add_quantity_combo.addItems([str(i + 1) for i in range(medicine.stock_quantity)])

    def load_remove_quantity(self):
        medicine_name = self.remove_combo.currentText()
        medicine = self.medicine_dao.get(name=medicine_name)

        self.remove_quantity_combo.clear()
        self.remove_quantity_combo.addItems([str(i + 1) for i in range(medicine.stock_quantity)])

    def load_medicines(self, combo):
        combo.clear()
        medicines = self.medicine_dao.get_all()
        combo.addItems([str(medicine) for medicine in medicines])

    def load_cart(self):
        self.cart = self.get_cart()
        medicines_from_db = self.medicine_dao.get(cart_id=self.cart.id)
        medicines = self.cart.medicines or medicines_from_db
        self.cart_table.setRowCount(len(self.cart.medicines))
        for row_idx, medicine in enumerate(self.cart.medicines):
            self.cart_table.setItem(row_idx, 0, QTableWidgetItem(str(medicine.id)))
            self.cart_table.setItem(row_idx, 1, QTableWidgetItem(medicine.name))
            self.cart_table.setItem(row_idx, 2, QTableWidgetItem(str(medicine.price)))
            self.cart_table.setItem(row_idx, 3, QTableWidgetItem(medicine.category.name if medicine.category else ""))
            self.cart_table.setItem(row_idx, 4, QTableWidgetItem(medicine.manufacturer.name if medicine.manufacturer else ""))
        return

    def add_to_cart(self):
        medicine_name = self.medicine_combo.currentText()
        medicine = self.medicine_dao.get(name=medicine_name)
        # quantity = int(self.add_quantity_combo.currentText())
        try:
            self.cart_service.add_medicine(medicine)
            if medicine not in self.cart.medicines:
                self.cart.medicines.append(medicine)
            self.load_cart()
        except ValueError:
            self.show_error('Лекарства нет в наличии')

    def remove_from_cart(self):
        medicine_name = self.remove_combo.currentText()
        medicine = self.medicine_dao.get(name=medicine_name)
        # quantity = int(self.remove_quantity_combo.currentText())
        self.cart_service.remove_medicine(medicine)
        if medicine in self.cart.medicines:
            self.cart.medicines.remove(medicine)
        self.load_cart()

    def calculate_total(self):
        price = self.cart_service.get_total_price()
        self.total_price_field.setText(str(price))
