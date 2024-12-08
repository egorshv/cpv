from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel

from src.base.dao import DAO
from src.base.screen import BaseScreen
from src.buyer.models import Buyer

class BuyerScreen(BaseScreen):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

        self.buyer_dao = DAO(
            engine=engine,
            model=Buyer,
        )

        # Форма добавления покупателя
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()
        self.create_button = QPushButton("Создать")
        self.create_button.clicked.connect(self.create_buyer)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Имя покупателя:"))
        form_layout.addWidget(self.first_name_input)
        form_layout.addWidget(QLabel("Фамилия покупателя:"))
        form_layout.addWidget(self.last_name_input)
        form_layout.addWidget(QLabel("Email покупателя:"))
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(QLabel("Адрес доставки покупателя:"))
        form_layout.addWidget(self.address_input)
        form_layout.addWidget(self.create_button)

        # Таблица покупателей
        self.buyer_table = QTableWidget()
        self.buyer_table.setColumnCount(4)
        self.buyer_table.setHorizontalHeaderLabels(["ID", "Имя", "Фамилия", "Email", "Адрес доставки"])

        self.layout.addLayout(form_layout)
        self.layout.addWidget(self.buyer_table)

        self.on_tab_selected()

    def on_tab_selected(self):
        self.load_data()

    def load_data(self):
        buyers = self.buyer_dao.get_all()
        self.buyer_table.setRowCount(len(buyers))
        for row_idx, buyer in enumerate(buyers):
            self.buyer_table.setItem(row_idx, 0, QTableWidgetItem(str(buyer.id)))
            self.buyer_table.setItem(row_idx, 1, QTableWidgetItem(buyer.first_name))
            self.buyer_table.setItem(row_idx, 2, QTableWidgetItem(buyer.last_name))
            self.buyer_table.setItem(row_idx, 3, QTableWidgetItem(buyer.email))
            self.buyer_table.setItem(row_idx, 4, QTableWidgetItem(buyer.delivery_address))
        return

    def create_buyer(self):
        """Создает нового покупателя."""
        fields = {
            "Имя": self.first_name_input,
            "Фамилия": self.last_name_input,
            "Email": self.email_input,
            "Адрес доставки": self.address_input,
        }
        if not self.validate_fields(fields):
            return

        try:
            buyer = Buyer(
                first_name=self.first_name_input.text(),
                last_name=self.last_name_input.text(),
                email=self.email_input.text(),
                delivery_address=self.address_input.text()
            )
            self.buyer_dao.create(buyer)
            self.load_data()
        except Exception as e:
            self.show_error(str(e))
