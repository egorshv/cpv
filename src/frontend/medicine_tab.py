from PyQt5.QtWidgets import QLineEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QLabel

from src.backend.dao import DAO
from src.frontend.base_tab import BaseTab
from src.backend.models.cart import Cart
from src.backend.models.category import MedicineCategory
from src.backend.models.manufacturer import Manufacturer
from src.backend.models.medicine import Medicine
from src.backend.facades.medicine import MedicineFacade


class MedicineTab(BaseTab):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.medicine_dao = DAO(
            engine=self.engine,
            model=Medicine,
        )
        self.manufacturer_dao = DAO(
            engine=self.engine,
            model=Manufacturer,
        )
        self.category_dao = DAO(
            engine=self.engine,
            model=MedicineCategory,
        )
        self.cart_dao = DAO(
            engine=self.engine,
            model=Cart,
        )

        # Создание формы для добавления лекарства
        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.description_input = QLineEdit()
        self.stock_input = QLineEdit()
        self.category_combo = QComboBox()
        self.manufacturer_combo = QComboBox()
        self.create_button = QPushButton("Создать")

        self.create_button.clicked.connect(self.create_medicine)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Название лекарства:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Цена:"))
        form_layout.addWidget(self.price_input)
        form_layout.addWidget(QLabel("Описание:"))
        form_layout.addWidget(self.description_input)
        form_layout.addWidget(QLabel("Количество в наличии:"))
        form_layout.addWidget(self.stock_input)
        form_layout.addWidget(QLabel("Категория:"))
        form_layout.addWidget(self.category_combo)
        form_layout.addWidget(QLabel("Производитель:"))
        form_layout.addWidget(self.manufacturer_combo)
        form_layout.addWidget(self.create_button)

        # Кнопки обновления цены и остатков
        self.update_price_button = QPushButton("Обновить цену")
        self.update_price_button.clicked.connect(self.update_price)

        self.update_stock_button = QPushButton("Обновить остатки")
        self.update_stock_button.clicked.connect(self.update_stock)
        self.medicine_to_update = QComboBox()

        update_layout = QHBoxLayout()
        update_layout.addWidget(QLabel('Лекарство для обновления:'))
        update_layout.addWidget(self.medicine_to_update)
        update_layout.addWidget(self.update_price_button)
        update_layout.addWidget(self.update_stock_button)

        # Таблица для вывода лекарств
        self.medicine_table = QTableWidget()
        self.medicine_table.setColumnCount(6)
        self.medicine_table.setHorizontalHeaderLabels(["ID", "Name", "Price", "Description", "Stock", "Category", "Manufacturer"])

        # Добавление элементов на экран
        self.layout.addLayout(form_layout)
        self.layout.addLayout(update_layout)
        self.layout.addWidget(self.medicine_table)

        self.on_tab_selected()

    def on_tab_selected(self):
        self.load_medicines(self.medicine_to_update)
        self.load_categories(self.category_combo)
        self.load_manufacturers(self.manufacturer_combo)
        self.load_data()

    def load_data(self):
        medicines = self.medicine_dao.get_all()
        self.medicine_table.setRowCount(len(medicines))
        for row_idx, medicine in enumerate(medicines):
            self.medicine_table.setItem(row_idx, 0, QTableWidgetItem(str(medicine.id)))
            self.medicine_table.setItem(row_idx, 1, QTableWidgetItem(medicine.name))
            self.medicine_table.setItem(row_idx, 2, QTableWidgetItem(str(medicine.price)))
            self.medicine_table.setItem(row_idx, 3, QTableWidgetItem(medicine.description))
            self.medicine_table.setItem(row_idx, 4, QTableWidgetItem(str(medicine.stock_quantity)))
            self.medicine_table.setItem(row_idx, 5, QTableWidgetItem(medicine.category.name if medicine.category else ""))
            self.medicine_table.setItem(row_idx, 6, QTableWidgetItem(medicine.manufacturer.name if medicine.manufacturer else ""))

    def load_categories(self, combo):
        combo.clear()
        categories = self.category_dao.get_all()
        combo.addItems([str(category) for category in categories])

    def load_manufacturers(self, combo):
        combo.clear()
        manufacturers = self.manufacturer_dao.get_all()
        combo.addItems([str(manufacturer) for manufacturer in manufacturers])

    def load_medicines(self, combo):
        combo.clear()
        medicines = self.medicine_dao.get_all()
        combo.addItems([str(medicine) for medicine in medicines])

    def update_price(self):
        medicine_name = self.medicine_to_update.currentText()
        if self.price_input.text().isdigit():
            new_price = int(self.price_input.text())
        else:
            self.show_error('Price must be number')
            return

        medicine = self.medicine_dao.get(name=medicine_name)
        service = MedicineFacade(medicine, self.medicine_dao)
        service.update_price(new_price)
        self.load_data()

    def update_stock(self):
        medicine_name = self.medicine_to_update.currentText()
        if self.stock_input.text().isdigit():
            new_stock = int(self.stock_input.text())
        else:
            self.show_error('Stock must be number')
            return

        medicine = self.medicine_dao.get(name=medicine_name)
        service = MedicineFacade(medicine, self.medicine_dao)
        service.update_stock(new_stock)
        self.load_data()

    def create_medicine(self):
        fields = {
            "Имя": self.name_input,
            "Цена": self.price_input,
            "Описание": self.description_input,
            "Количество в наличии": self.stock_input,
        }
        if not self.validate_fields(fields):
            return

        try:
            category_name = self.category_combo.currentText()
            category = self.category_dao.get(name=category_name)

            manufacturer_name = self.manufacturer_combo.currentText()
            manufacturer = self.manufacturer_dao.get(name=manufacturer_name)

            medicine = Medicine(
                name=self.name_input.text(),
                price=float(self.price_input.text()),
                description=self.description_input.text(),
                stock_quantity=int(self.stock_input.text()),
                category=category,
                manufacturer=manufacturer,
            )
            self.medicine_dao.create(medicine)
            self.load_data()
        except Exception as e:
            self.show_error(str(e))
