from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from src.base.screen import BaseScreen
from src.manufacturer.models import Manufacturer

class ManufacturerScreen(BaseScreen):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

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

        self.load_data()

    def load_data(self):
        """Загружает данные в таблицу."""
        # manufacturers = self.db_session.query(Manufacturer).all()
        # self.manufacturer_table.setRowCount(len(manufacturers))
        # for row_idx, manufacturer in enumerate(manufacturers):
        #     self.manufacturer_table.setItem(row_idx, 0, QTableWidgetItem(str(manufacturer.id)))
        #     self.manufacturer_table.setItem(row_idx, 1, QTableWidgetItem(manufacturer.name))
        #     self.manufacturer_table.setItem(row_idx, 2, QTableWidgetItem(manufacturer.country_foreign))
        pass

    def create_manufacturer(self):
        """Создает нового производителя."""
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
            self.db_session.add(manufacturer)
            self.db_session.commit()
            self.load_data()
        except Exception as e:
            self.show_error(str(e))
