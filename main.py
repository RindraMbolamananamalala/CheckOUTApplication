
import sys

from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.ui_test_report_result import UITestReportResult
from PRESENTATION.HMI.ui_quality_inspector_code_scan import UIQualityInspectorCodeScan
from PRESENTATION.VIEW.barcode_scan_view import BarcodeScanView
from PRESENTATION.CONTROLLER.rework_check_out_controller import ReworkCheckOUTController

if __name__ == '__main__':
    application = QApplication(sys.argv)

    controller = ReworkCheckOUTController()

    # Application has started...
    LOGGER.info("Check OUT Application has started")

    sys.exit(application.exec_())

