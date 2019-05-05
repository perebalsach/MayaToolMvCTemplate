import os
import sys
import shiboken2
import maya.cmds as cmds
import maya.OpenMayaUI as MayaUI
from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets

SCRIPT_LOC = os.path.dirname(__file__)


def load_ui_widget(ui_filename, parent=None):
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(ui_filename)
    ui_file.open(QtCore.QFile.ReadOnly)
    ui = loader.load(ui_file, parent)
    ui_file.close()
    return ui


def run_maya_template_ui():

    try:
        ui.deleteLater()
    except:
        pass
    ui = TemplateUi()


    # """Command within Maya to run this script"""
    # if not (cmds.window("templateUi", exists=True)):
    #     TemplateUi()
    # else:
    #     sys.stdout.write("Tool is already open!\n")


class TemplateUi(QtWidgets.QMainWindow):
    def __init__(self):
        main_ui = os.path.join(SCRIPT_LOC, "view", "base_view.ui" )
        maya_main = shiboken2.wrapInstance(long(MayaUI.MQtUtil.mainWindow()), QtWidgets.QWidget)
        super(TemplateUi, self).__init__(maya_main)

        # main window load / settings
        self.main_window_ui = load_ui_widget(main_ui, maya_main)
        self.main_window_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.main_window_ui.destroyed.connect(self.on_exit_code)
        self.main_window_ui.show()

        self.make_connections()

    def make_connections(self):
        # the lambda: is (in my words) a handy way to pass an argument to our function without python running it.
        # self.main_window_ui.addCube_btn.clicked.connect(lambda: self.some_function("I'm a function!"))
        pass

    def on_exit_code(self):
        sys.stdout.write("UI successfully closed\n")
        self.deleteLater()

    def some_function(self, someArg):
        print someArg