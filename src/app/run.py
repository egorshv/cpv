import sys

from PyQt5.QtWidgets import QApplication
from sqlalchemy.engine import create_engine

from src.settings import DSN
from src.app.screen import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    engine = create_engine(DSN)
    main_window = MainWindow(engine)
    main_window.show()
    sys.exit(app.exec_())