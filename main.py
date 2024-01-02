
import sys

from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.CONTROLLER.rework_check_out_controller import ReworkCheckOUTController
from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code_scan import UIQualityInspectorCodeScan
from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code_verification import UIQualityInspectorCodeVerification

if __name__ == '__main__':
    application = QApplication(sys.argv)

    #controller = ReworkCheckOUTController()

    ui = UIQualityInspectorCodeVerification(QMainWindow())
    ui.get_main_window().show()

    # Application has started...
    LOGGER.info("Check OUT Application has started")

    sys.exit(application.exec_())

