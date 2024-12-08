from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel

from src.base.dao import DAO
from src.base.screen import BaseScreen
from src.manufacturer.models import Manufacturer

class ManufacturerScreen(BaseScreen):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

        self.manufacturer_dao = DAO(
            engine=engine,
            model=Manufacturer,
        )

        # Форма добавления производителя
        self.name_input = QLineEdit()
        self.country_input = QLineEdit()
        self.create_button = QPushButton("Создать")
        self.create_button.clicked.connect(self.create_manufacturer)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Название производителя:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Страна производителя:"))
        form_layout.addWidget(self.country_input)
        form_layout.addWidget(self.create_button)

        # Таблица производителей
        self.manufacturer_table = QTableWidget()
        self.manufacturer_table.setColumnCount(3)
        self.manufacturer_table.setHorizontalHeaderLabels(["ID", "Название", "Страна"])

        self.layout.addLayout(form_layout)
        self.layout.addWidget(self.manufacturer_table)

        self.on_tab_selected()

    def on_tab_selected(self):
        self.load_data()

    def load_data(self):
        manufacturers = self.manufacturer_dao.get_all()
        self.manufacturer_table.setRowCount(len(manufacturers))
        for row_idx, manufacturer in enumerate(manufacturers):
            self.manufacturer_table.setItem(row_idx, 0, QTableWidgetItem(str(manufacturer.id)))
            self.manufacturer_table.setItem(row_idx, 1, QTableWidgetItem(manufacturer.name))
            self.manufacturer_table.setItem(row_idx, 2, QTableWidgetItem(manufacturer.country_foreign))
        return

    def create_manufacturer(self):
        fields = {
            "Название": self.name_input,
            "Страна": self.country_input,
        }
        if not self.validate_fields(fields):
            return

        try:
            manufacturer = Manufacturer(
                name=self.name_input.text(),
                country_foreign=self.country_input.text()
            )
            self.manufacturer_dao.create(manufacturer)
            self.load_data()
        except Exception as e:
            self.show_error(str(e))
