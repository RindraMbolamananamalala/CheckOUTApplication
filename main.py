
import sys

from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.ui_test_report_result import UITestReportResult
from PRESENTATION.HMI.ui_quality_inspector_code_scan import UIQualityInspectorCodeScan
from PRESENTATION.VIEW.barcode_scan_view import BarcodeScanView

if __name__ == '__main__':
    application = QApplication(sys.argv)

    # Application has started...
    LOGGER.info("Check OUT Application has started")

    hmi = UIQualityInspectorCodeScan(QMainWindow())
    hmi.get_main_window().show()

    sys.exit(application.exec_())

