
import sys

from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.VIEW.barcode_scan_view import BarcodeScanView

if __name__ == '__main__':
    application = QApplication(sys.argv)

    view = BarcodeScanView()
    view.show_window()

    # Application has started...
    LOGGER.info("Check OUT Application has started")

    sys.exit(application.exec_())

