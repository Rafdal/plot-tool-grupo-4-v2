# Form implementation generated from reading ui file 'UI_AddTracePopUp.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddTracePopUp(object):
    def setupUi(self, AddTracePopUp):
        AddTracePopUp.setObjectName("AddTracePopUp")
        AddTracePopUp.resize(849, 661)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddTracePopUp.sizePolicy().hasHeightForWidth())
        AddTracePopUp.setSizePolicy(sizePolicy)
        AddTracePopUp.setMaximumSize(QtCore.QSize(16777215, 1032))
        self.gridLayout_2 = QtWidgets.QGridLayout(AddTracePopUp)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(6, -1, -1, -1)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(parent=AddTracePopUp)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 832, 240))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.SignalGroupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignalGroupBox.sizePolicy().hasHeightForWidth())
        self.SignalGroupBox.setSizePolicy(sizePolicy)
        self.SignalGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.SignalGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SignalGroupBox.setObjectName("SignalGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.SignalGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.XAxisDataLabel = QtWidgets.QLabel(parent=self.SignalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XAxisDataLabel.sizePolicy().hasHeightForWidth())
        self.XAxisDataLabel.setSizePolicy(sizePolicy)
        self.XAxisDataLabel.setObjectName("XAxisDataLabel")
        self.gridLayout_3.addWidget(self.XAxisDataLabel, 0, 0, 1, 1)
        self.XOpLE = QtWidgets.QLineEdit(parent=self.SignalGroupBox)
        self.XOpLE.setObjectName("XOpLE")
        self.gridLayout_3.addWidget(self.XOpLE, 0, 3, 1, 1)
        self.XOpLabel = QtWidgets.QLabel(parent=self.SignalGroupBox)
        self.XOpLabel.setObjectName("XOpLabel")
        self.gridLayout_3.addWidget(self.XOpLabel, 0, 2, 1, 1)
        self.XDataCB = QtWidgets.QComboBox(parent=self.SignalGroupBox)
        self.XDataCB.setMinimumSize(QtCore.QSize(200, 0))
        self.XDataCB.setObjectName("XDataCB")
        self.gridLayout_3.addWidget(self.XDataCB, 0, 1, 1, 1)
        self.YAxisQuantSpinBox = QtWidgets.QSpinBox(parent=self.SignalGroupBox)
        self.YAxisQuantSpinBox.setMinimum(1)
        self.YAxisQuantSpinBox.setMaximum(10)
        self.YAxisQuantSpinBox.setProperty("value", 2)
        self.YAxisQuantSpinBox.setObjectName("YAxisQuantSpinBox")
        self.gridLayout_3.addWidget(self.YAxisQuantSpinBox, 0, 4, 1, 1)
        self.gridLayout_5.addWidget(self.SignalGroupBox, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea, 4, 1, 1, 6)
        self.SignalRadioButton = QtWidgets.QRadioButton(parent=AddTracePopUp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignalRadioButton.sizePolicy().hasHeightForWidth())
        self.SignalRadioButton.setSizePolicy(sizePolicy)
        self.SignalRadioButton.setObjectName("SignalRadioButton")
        self.gridLayout_2.addWidget(self.SignalRadioButton, 2, 4, 1, 1)
        self.BodeGroupBox = QtWidgets.QGroupBox(parent=AddTracePopUp)
        self.BodeGroupBox.setObjectName("BodeGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.BodeGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.FreqOpLE = QtWidgets.QLineEdit(parent=self.BodeGroupBox)
        self.FreqOpLE.setObjectName("FreqOpLE")
        self.gridLayout_4.addWidget(self.FreqOpLE, 0, 3, 1, 1)
        self.FreqDataCB = QtWidgets.QComboBox(parent=self.BodeGroupBox)
        self.FreqDataCB.setMinimumSize(QtCore.QSize(200, 0))
        self.FreqDataCB.setObjectName("FreqDataCB")
        self.gridLayout_4.addWidget(self.FreqDataCB, 0, 1, 1, 1)
        self.ModAxisLabel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModAxisLabel.sizePolicy().hasHeightForWidth())
        self.ModAxisLabel.setSizePolicy(sizePolicy)
        self.ModAxisLabel.setObjectName("ModAxisLabel")
        self.gridLayout_4.addWidget(self.ModAxisLabel, 1, 0, 1, 1)
        self.YOpLabel_2 = QtWidgets.QLabel(parent=self.BodeGroupBox)
        self.YOpLabel_2.setObjectName("YOpLabel_2")
        self.gridLayout_4.addWidget(self.YOpLabel_2, 2, 2, 1, 1)
        self.BodeTraceNameLabel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodeTraceNameLabel.sizePolicy().hasHeightForWidth())
        self.BodeTraceNameLabel.setSizePolicy(sizePolicy)
        self.BodeTraceNameLabel.setObjectName("BodeTraceNameLabel")
        self.gridLayout_4.addWidget(self.BodeTraceNameLabel, 7, 0, 1, 1)
        self.PhaseOpLE = QtWidgets.QLineEdit(parent=self.BodeGroupBox)
        self.PhaseOpLE.setObjectName("PhaseOpLE")
        self.gridLayout_4.addWidget(self.PhaseOpLE, 2, 3, 1, 1)
        self.XOpLabel_2 = QtWidgets.QLabel(parent=self.BodeGroupBox)
        self.XOpLabel_2.setObjectName("XOpLabel_2")
        self.gridLayout_4.addWidget(self.XOpLabel_2, 1, 2, 1, 1)
        self.BodeColorLabel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodeColorLabel.sizePolicy().hasHeightForWidth())
        self.BodeColorLabel.setSizePolicy(sizePolicy)
        self.BodeColorLabel.setObjectName("BodeColorLabel")
        self.gridLayout_4.addWidget(self.BodeColorLabel, 5, 0, 1, 1)
        self.PhaseDataCB = QtWidgets.QComboBox(parent=self.BodeGroupBox)
        self.PhaseDataCB.setObjectName("PhaseDataCB")
        self.gridLayout_4.addWidget(self.PhaseDataCB, 2, 1, 1, 1)
        self.FrequencyLAbel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrequencyLAbel.sizePolicy().hasHeightForWidth())
        self.FrequencyLAbel.setSizePolicy(sizePolicy)
        self.FrequencyLAbel.setObjectName("FrequencyLAbel")
        self.gridLayout_4.addWidget(self.FrequencyLAbel, 0, 0, 1, 1)
        self.ModDataCB = QtWidgets.QComboBox(parent=self.BodeGroupBox)
        self.ModDataCB.setMinimumSize(QtCore.QSize(200, 0))
        self.ModDataCB.setObjectName("ModDataCB")
        self.gridLayout_4.addWidget(self.ModDataCB, 1, 1, 1, 1)
        self.FaseAxisLabel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        self.FaseAxisLabel.setObjectName("FaseAxisLabel")
        self.gridLayout_4.addWidget(self.FaseAxisLabel, 2, 0, 1, 1)
        self.ModOpLE = QtWidgets.QLineEdit(parent=self.BodeGroupBox)
        self.ModOpLE.setObjectName("ModOpLE")
        self.gridLayout_4.addWidget(self.ModOpLE, 1, 3, 1, 1)
        self.XOpLabel_3 = QtWidgets.QLabel(parent=self.BodeGroupBox)
        self.XOpLabel_3.setObjectName("XOpLabel_3")
        self.gridLayout_4.addWidget(self.XOpLabel_3, 0, 2, 1, 1)
        self.BodeLineTypeLabel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodeLineTypeLabel.sizePolicy().hasHeightForWidth())
        self.BodeLineTypeLabel.setSizePolicy(sizePolicy)
        self.BodeLineTypeLabel.setObjectName("BodeLineTypeLabel")
        self.gridLayout_4.addWidget(self.BodeLineTypeLabel, 6, 0, 1, 1)
        self.BodeTraceNameLE = QtWidgets.QLineEdit(parent=self.BodeGroupBox)
        self.BodeTraceNameLE.setObjectName("BodeTraceNameLE")
        self.gridLayout_4.addWidget(self.BodeTraceNameLE, 7, 1, 1, 1)
        self.BodeTraceTypeCB = QtWidgets.QComboBox(parent=self.BodeGroupBox)
        self.BodeTraceTypeCB.setObjectName("BodeTraceTypeCB")
        self.gridLayout_4.addWidget(self.BodeTraceTypeCB, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BodeColorButton = QtWidgets.QPushButton(parent=self.BodeGroupBox)
        self.BodeColorButton.setMinimumSize(QtCore.QSize(30, 30))
        self.BodeColorButton.setMaximumSize(QtCore.QSize(30, 30))
        self.BodeColorButton.setText("")
        self.BodeColorButton.setObjectName("BodeColorButton")
        self.horizontalLayout_2.addWidget(self.BodeColorButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        self.MarkerLabel = QtWidgets.QLabel(parent=self.BodeGroupBox)
        self.MarkerLabel.setObjectName("MarkerLabel")
        self.gridLayout_4.addWidget(self.MarkerLabel, 6, 2, 1, 1)
        self.MarkersCB = QtWidgets.QComboBox(parent=self.BodeGroupBox)
        self.MarkersCB.setObjectName("MarkersCB")
        self.gridLayout_4.addWidget(self.MarkersCB, 6, 3, 1, 1)
        self.gridLayout_2.addWidget(self.BodeGroupBox, 3, 1, 1, 6)
        self.BodeRadioButton = QtWidgets.QRadioButton(parent=AddTracePopUp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodeRadioButton.sizePolicy().hasHeightForWidth())
        self.BodeRadioButton.setSizePolicy(sizePolicy)
        self.BodeRadioButton.setChecked(True)
        self.BodeRadioButton.setObjectName("BodeRadioButton")
        self.gridLayout_2.addWidget(self.BodeRadioButton, 2, 1, 1, 3)
        self.Dir2FileLabel = QtWidgets.QLabel(parent=AddTracePopUp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dir2FileLabel.sizePolicy().hasHeightForWidth())
        self.Dir2FileLabel.setSizePolicy(sizePolicy)
        self.Dir2FileLabel.setObjectName("Dir2FileLabel")
        self.gridLayout_2.addWidget(self.Dir2FileLabel, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Dir2FileLE = QtWidgets.QLineEdit(parent=AddTracePopUp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dir2FileLE.sizePolicy().hasHeightForWidth())
        self.Dir2FileLE.setSizePolicy(sizePolicy)
        self.Dir2FileLE.setMinimumSize(QtCore.QSize(0, 0))
        self.Dir2FileLE.setReadOnly(True)
        self.Dir2FileLE.setObjectName("Dir2FileLE")
        self.horizontalLayout.addWidget(self.Dir2FileLE)
        self.Dir2FileButton = QtWidgets.QPushButton(parent=AddTracePopUp)
        self.Dir2FileButton.setObjectName("Dir2FileButton")
        self.horizontalLayout.addWidget(self.Dir2FileButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 5)
        self.MonteCarloGroupBox = QtWidgets.QGroupBox(parent=AddTracePopUp)
        self.MonteCarloGroupBox.setEnabled(True)
        self.MonteCarloGroupBox.setObjectName("MonteCarloGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.MonteCarloGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.MonteCarloGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.StepQuantSpinBox = QtWidgets.QSpinBox(parent=self.MonteCarloGroupBox)
        self.StepQuantSpinBox.setMinimum(1)
        self.StepQuantSpinBox.setProperty("value", 10)
        self.StepQuantSpinBox.setObjectName("StepQuantSpinBox")
        self.gridLayout.addWidget(self.StepQuantSpinBox, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.MonteCarloGroupBox, 8, 2, 2, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=AddTracePopUp)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 9, 6, 1, 1)
        self.IsMCCheckBox = QtWidgets.QCheckBox(parent=AddTracePopUp)
        self.IsMCCheckBox.setObjectName("IsMCCheckBox")
        self.gridLayout_2.addWidget(self.IsMCCheckBox, 8, 1, 1, 1)
        self.FileDropBox = QtWidgets.QFrame(parent=AddTracePopUp)
        self.FileDropBox.setMinimumSize(QtCore.QSize(0, 50))
        self.FileDropBox.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.FileDropBox.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.FileDropBox.setObjectName("FileDropBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FileDropBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.FileDropBox)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2.addWidget(self.FileDropBox, 0, 1, 1, 6)

        self.retranslateUi(AddTracePopUp)
        self.buttonBox.accepted.connect(AddTracePopUp.accept) # type: ignore
        self.buttonBox.rejected.connect(AddTracePopUp.reject) # type: ignore
        self.Dir2FileButton.clicked.connect(AddTracePopUp.BrowseFile) # type: ignore
        self.IsMCCheckBox.toggled['bool'].connect(self.MonteCarloGroupBox.setVisible) # type: ignore
        self.BodeRadioButton.toggled['bool'].connect(self.BodeGroupBox.setVisible) # type: ignore
        self.YAxisQuantSpinBox.valueChanged['int'].connect(AddTracePopUp.YAxisQuantUpdate) # type: ignore
        self.BodeColorButton.clicked.connect(AddTracePopUp.ChooseBodeColor) # type: ignore
        self.SignalRadioButton.toggled['bool'].connect(self.scrollArea.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AddTracePopUp)

    def retranslateUi(self, AddTracePopUp):
        _translate = QtCore.QCoreApplication.translate
        AddTracePopUp.setWindowTitle(_translate("AddTracePopUp", "Añadir Linea"))
        self.SignalGroupBox.setTitle(_translate("AddTracePopUp", "Señal"))
        self.XAxisDataLabel.setText(_translate("AddTracePopUp", "Datos para Eje X"))
        self.XOpLabel.setText(_translate("AddTracePopUp", "Operacion"))
        self.SignalRadioButton.setText(_translate("AddTracePopUp", "Señal"))
        self.BodeGroupBox.setTitle(_translate("AddTracePopUp", "Bode"))
        self.ModAxisLabel.setText(_translate("AddTracePopUp", "Modulo"))
        self.YOpLabel_2.setText(_translate("AddTracePopUp", "Operacion"))
        self.BodeTraceNameLabel.setText(_translate("AddTracePopUp", "Nombre de la curva"))
        self.XOpLabel_2.setText(_translate("AddTracePopUp", "Operacion"))
        self.BodeColorLabel.setText(_translate("AddTracePopUp", "Color"))
        self.FrequencyLAbel.setText(_translate("AddTracePopUp", "Frecuencia"))
        self.FaseAxisLabel.setText(_translate("AddTracePopUp", "Fase"))
        self.XOpLabel_3.setText(_translate("AddTracePopUp", "Operacion"))
        self.BodeLineTypeLabel.setText(_translate("AddTracePopUp", "Tipo de Linea"))
        self.MarkerLabel.setText(_translate("AddTracePopUp", "Marcadores"))
        self.BodeRadioButton.setText(_translate("AddTracePopUp", "Bode"))
        self.Dir2FileLabel.setText(_translate("AddTracePopUp", "Direccion al archivo"))
        self.Dir2FileButton.setText(_translate("AddTracePopUp", "Browse..."))
        self.MonteCarloGroupBox.setTitle(_translate("AddTracePopUp", "Monte Carlo"))
        self.label_3.setText(_translate("AddTracePopUp", "Cantidad de pasos a tomar"))
        self.IsMCCheckBox.setText(_translate("AddTracePopUp", "MonteCarlo? (Solo Spice)"))
        self.label.setText(_translate("AddTracePopUp", "Arrastra y suelta un archivo"))
