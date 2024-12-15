from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel

from src.base.dao import DAO
from src.base.tab import BaseTab
from src.category.models import MedicineCategory
from src.medicine.models import Medicine


class MedicineCategoryTab(BaseTab):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.category_dao = DAO(
            engine=engine,
            model=MedicineCategory,
        )
        self.medicine_dao = DAO(
            engine=engine,
            model=Medicine,
        )

        # Форма добавления категории
        self.name_input = QLineEdit()
        self.description_input = QLineEdit()
        self.create_button = QPushButton("Создать")
        self.create_button.clicked.connect(self.create_category)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Имя:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Описание:"))
        form_layout.addWidget(self.description_input)
        form_layout.addWidget(self.create_button)

        # Таблица категорий
        self.category_table = QTableWidget()
        self.category_table.setColumnCount(3)
        self.category_table.setHorizontalHeaderLabels(["ID", "Название", "Описание"])

        self.layout.addLayout(form_layout)
        self.layout.addWidget(self.category_table)

        self.on_tab_selected()

    def on_tab_selected(self):
        self.load_data()

    def load_data(self):
        categories = self.category_dao.get_all()
        self.category_table.setRowCount(len(categories))
        for row_idx, category in enumerate(categories):
            self.category_table.setItem(row_idx, 0, QTableWidgetItem(str(category.id)))
            self.category_table.setItem(row_idx, 1, QTableWidgetItem(category.name))
            self.category_table.setItem(row_idx, 2, QTableWidgetItem(category.description))

    def create_category(self):
        fields = {
            "Название": self.name_input,
            "Описание": self.description_input,
        }
        if not self.validate_fields(fields):
            return

        try:
            category = MedicineCategory(
                name=self.name_input.text(),
                description=self.description_input.text()
            )
            self.category_dao.create(category)
            self.load_data()
        except Exception as e:
            self.show_error(str(e))
