import os
import maya.OpenMayaUI as omUI
from shiboken2 import wrapInstance
from PySide2 import QtWidgets, QtCore, QtUiTools


script_path = os.path.dirname(__file__)


def get_maya_window():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """
    ptr = omUI.MQtUtil.mainWindow()
    if ptr is not None:
        return wrapInstance(long(ptr), QtWidgets.QWidget)


class MayaTemplateController(QtWidgets.QMainWindow):
    def __init__(self, parent=get_maya_window()):
        super(MayaTemplateController, self).__init__(parent)

        ui_file_path = os.path.join(script_path, "view", "base_view.ui")
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile(ui_file_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        self.ui.show()

