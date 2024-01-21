
import sys

from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.CONTROLLER.rework_check_out_controller import ReworkCheckOUTController
from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code_scan import UIQualityInspectorCodeScan
from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code_verification import UIQualityInspectorCodeVerification

from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.rework_check_out_as_impl import ReworkCheckOUTASImpl
from DATA_ACCESS.DAO.IMPL.rework_check_out_application_file_dao_impl import ReworkCheckOUTApplicationFileDAOImpl

if __name__ == '__main__':
    application = QApplication(sys.argv)

    controller = ReworkCheckOUTController()

    # Application has started...
    LOGGER.info("Check OUT Application has started")

    sys.exit(application.exec_())

