from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox

from src.cart.models import Cart


class BaseScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

    def get_cart(self):
        carts = self.cart_dao.get_all()
        if not carts:
            cart = Cart()
            self.cart_dao.create(cart)
            return cart
        return carts[0]

    def show_error(self, message: str):
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Critical)
        error_box.setText(message)
        error_box.setWindowTitle("Ошибка")
        error_box.exec_()

    def validate_fields(self, fields):
        for field_name, field in fields.items():
            if not field.text().strip():
                self.show_error(f"Поле '{field_name}' не может быть пустым.")
                return False
        return True
