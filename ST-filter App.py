import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests
import seaborn as sns
import matplotlib.pyplot as plt
from venn import venn
import shutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        MainWindow.setFont(font)

        self.Result = QtWidgets.QTextEdit(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(300, 70, 800, 700))
        self.Result.setObjectName("Result")
        self.Result.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        t = open("test.txt", "r")
        self.Result.setText(t.read())


        self.plot = QtWidgets.QLabel(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(1150, 70, 600, 700))
        self.plot.setAcceptDrops(True)
        self.plot.setAutoFillBackground(True)
        self.plot.setText("")
        self.plot.setPixmap(QtGui.QPixmap("bsp.png"))
        self.plot.setObjectName("plot")

        self.plotText = QtWidgets.QLabel(self.centralwidget)
        self.plotText.setGeometry(QtCore.QRect(1150, 40,200, 23))
        self.plotText.setObjectName("plotText")
        self.plotText.setFont(font)




        open_icon = self.style().standardIcon(QtWidgets.QStyle.SP_FileDialogStart)
        self.openfile = QtWidgets.QToolButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(120, 10, 35, 25))
        self.openfile.setObjectName("openfile")
        self.openfile.clicked.connect(MainWindow.openFile)
        self.openfile.setIcon(open_icon)
        self.openfile.setStyleSheet("background-color : gold")
        # notize geben
        self.openfile.setToolTip('please import new File!')

        self.showFile = QtWidgets.QToolButton(self.centralwidget)
        self.showFile.setGeometry(QtCore.QRect(170, 10, 35, 25))
        self.showFile.setObjectName("showFile")
        self.showFile.clicked.connect(MainWindow.showfile)
        self.showFile.setStyleSheet("background-color : gold")
        self.showFile.setToolTip('Show your data in the display field!')
   #######################################################################################
        self.A = QtWidgets.QLabel(self.centralwidget)
        self.A.setGeometry(QtCore.QRect(30, 90, 55, 23))
        self.A.setObjectName("A")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.A.setFont(font)

        self.FilterFile = QtWidgets.QPushButton(self.centralwidget)
        self.FilterFile.setGeometry(QtCore.QRect(100, 90, 150, 31))
        self.FilterFile.setObjectName("FilterFile")
        self.FilterFile.clicked.connect(MainWindow.filter)
        self.FilterFile.setStyleSheet("background-color : gold")
        self.FilterFile.setToolTip('Identifiers only found in treatments')


        self.ShowFilter = QtWidgets.QPushButton(self.centralwidget)
        self.ShowFilter.setGeometry(QtCore.QRect(100, 130, 150, 31))
        self.ShowFilter.setObjectName("ShowFilter")
        self.ShowFilter.clicked.connect(MainWindow.showfilter)
        self.ShowFilter.setStyleSheet("background-color : gold")
        self.ShowFilter.setToolTip('Show your result in the display field')
#################################################################################################

        self.B = QtWidgets.QLabel(self.centralwidget)
        self.B.setGeometry(QtCore.QRect(30, 200, 55, 23))
        self.B.setObjectName("B")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.B.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.B2 = QtWidgets.QLabel(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(100, 200, 150, 13))
        self.B2.setObjectName("B2")
        self.B2.setFont(font)

        self.B3 = QtWidgets.QLabel(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(100, 220, 150, 13))
        self.B3.setObjectName("B3")
        self.B3.setFont(font)

        self.B4 = QtWidgets.QLabel(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(100, 240, 150, 13))
        self.B4.setObjectName("B4")
        self.B4.setFont(font)


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(190, 275, 70, 13))
        self.label2.setObjectName("label2")
        self.label2.setFont(font)


        self.SD = QtWidgets.QTextEdit(self.centralwidget)
        self.SD.setGeometry(QtCore.QRect(100, 270, 85, 26))
        self.SD.setObjectName("SD")

        self.meanSd = QtWidgets.QPushButton(self.centralwidget)
        self.meanSd.setGeometry(QtCore.QRect(100, 300, 150, 31))
        self.meanSd.setObjectName("meanSd")
        self.meanSd.setStyleSheet("background-color : gold")
        self.meanSd.clicked.connect(MainWindow.mean_std)


        self.MeanSDresult = QtWidgets.QPushButton(self.centralwidget)
        self.MeanSDresult.setGeometry(QtCore.QRect(100, 340, 150, 31))
        self.MeanSDresult.setObjectName("MeanSDresult")
        self.MeanSDresult.setStyleSheet("background-color : gold")
        self.MeanSDresult.clicked.connect(MainWindow.show_meansd)
        self.MeanSDresult.setToolTip('Show your result in the display field')
    #######################################################################################
        self.Methode3 = QtWidgets.QComboBox(self.centralwidget)
        self.Methode3.setGeometry(QtCore.QRect(100, 400, 150, 25))
        self.Methode3.setObjectName("Methode3")
        self.Methode3.addItem("")
        self.Methode3.addItem("")

        self.C = QtWidgets.QLabel(self.centralwidget)
        self.C.setGeometry(QtCore.QRect(30, 400, 55, 23))
        self.C.setObjectName("C")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.C.setFont(font)

        self.Methode = QtWidgets.QComboBox(self.centralwidget)
        self.Methode.setGeometry(QtCore.QRect(100, 430, 150, 25))
        self.Methode.setObjectName("Methode")
        self.Methode.addItem("")
        self.Methode.addItem("")

        self.pValue = QtWidgets.QTextEdit(self.centralwidget)
        self.pValue.setGeometry(QtCore.QRect(140, 470, 100, 26))
        self.pValue.setObjectName("pValue")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(100, 470, 25, 16))
        self.label3.setObjectName("label3")
        font.setItalic(True)
        self.label3.setFont(font)

        self.label31 = QtWidgets.QLabel(self.centralwidget)
        self.label31.setGeometry(QtCore.QRect(100, 500, 80, 16))
        self.label31.setObjectName("label31")
        font.setItalic(True)
        self.label31.setFont(font)

        self.T_test = QtWidgets.QPushButton(self.centralwidget)
        self.T_test.setGeometry(QtCore.QRect(100, 530, 150, 30))
        self.T_test.setObjectName("T_test")
        self.T_test.setStyleSheet("background-color : gold")
        self.T_test.clicked.connect(MainWindow.ttest)


        self.tResult = QtWidgets.QPushButton(self.centralwidget)
        self.tResult.setGeometry(QtCore.QRect(100, 570, 150, 31))
        self.tResult.setObjectName("tResult")
        self.tResult.setStyleSheet("background-color : gold")
        self.tResult.clicked.connect(MainWindow.ShowT)
        self.tResult.setToolTip('Show your result in the display field')
#################################################################################################
        self.D = QtWidgets.QLabel(self.centralwidget)
        self.D.setGeometry(QtCore.QRect(100, 650, 150, 20))
        self.D.setObjectName("D")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.D.setFont(font)

        self.venn = QtWidgets.QPushButton(self.centralwidget)
        self.venn.setGeometry(QtCore.QRect(100, 680, 150, 30))
        self.venn.setObjectName("venn")
        self.venn.setStyleSheet("background-color : gold")
        self.venn.clicked.connect(MainWindow.vennTest)

        self.vResult = QtWidgets.QPushButton(self.centralwidget)
        self.vResult.setGeometry(QtCore.QRect(100, 720, 150, 31))
        self.vResult.setObjectName("tResult")
        self.vResult.setStyleSheet("background-color : gold")
        self.vResult.clicked.connect(MainWindow.ShowV)
        self.vResult.setToolTip('Show your result in the display field')
########################################################################################################



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 150, 13))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label.setFont(font)

        self.baitBox = QtWidgets.QComboBox(self.centralwidget)
        self.baitBox.setGeometry(QtCore.QRect(450, 20, 60, 25))
        self.baitBox.setObjectName("baitBox")
        self.baitBox.addItem("")
        self.baitBox.addItem("")

        self.bait = QtWidgets.QTextEdit(self.centralwidget)
        self.bait.setGeometry(QtCore.QRect(520, 20, 150, 25))
        self.bait.setObjectName("bait")

        self.baitgo = QtWidgets.QToolButton(self.centralwidget)
        self.baitgo.setGeometry(QtCore.QRect(700, 20, 35, 25))
        self.baitgo.setObjectName("baitgo")
        self.baitgo.clicked.connect(MainWindow.withbait)
        self.baitgo.setStyleSheet("background-color : gold")

        self.baitshow = QtWidgets.QToolButton(self.centralwidget)
        self.baitshow.setGeometry(QtCore.QRect(740, 20, 35, 25))
        self.baitshow.setObjectName("baitshow")
        self.baitshow.clicked.connect(MainWindow.showbait)
        self.baitshow.setStyleSheet("background-color : gold")
        self.baitshow.setToolTip('Show your data in the display field!')

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openfile.setText(_translate("MainWindow", "..."))
        self.showFile.setText(_translate("MainWindow", "Show"))
        self.FilterFile.setText(_translate("MainWindow", "Special treatment"))
        self.ShowFilter.setText(_translate("MainWindow", "Result"))
        self.meanSd.setText(_translate("MainWindow", "Mean"))
        self.MeanSDresult.setText(_translate("MainWindow", "Result"))
        self.T_test.setText(_translate("MainWindow", "Tests"))
        self.tResult.setText(_translate("MainWindow", "Result"))

        self.label.setText(_translate("MainWindow", "Normalization with bait"))
        self.label2.setText(_translate("MainWindow", "x SD (>0)"))
        self.B2.setText(_translate("MainWindow", "Fold change"))
        self.label3.setText(_translate("MainWindow", "p|f<"))
        self.B3.setText(_translate("MainWindow","Treatment/control)>SD"))
        self.B4.setText(_translate("MainWindow", "Treatment/control)<SD"))

        self.label31.setText(_translate("MainWindow", "(0<p<1)"))



        self.venn.setText(_translate("MainWindow", "A U B U C"))
        self.vResult.setText(_translate("MainWindow", "Result"))


        self.Methode.setItemText(0, _translate("MainWindow", "p-value"))
        self.Methode.setItemText(1, _translate("MainWindow", "fdr_bh"))


        self.Methode3.setItemText(0, _translate("MainWindow", "Student's t-test"))
        self.Methode3.setItemText(1, _translate("MainWindow", "Welch's t-test"))

        self.baitBox.setItemText(0, _translate("MainWindow", "No"))
        self.baitBox.setItemText(1, _translate("MainWindow", "Yes"))

        self.baitgo.setText(_translate("MainWindow", "Go"))
        self.baitshow.setText(_translate("MainWindow", "Show"))

        self.A.setText(_translate("MainWindow", "Filter A"))
        self.B.setText(_translate("MainWindow", "Filter B"))
        self.C.setText(_translate("MainWindow", "Filter C"))
        self.D.setText(_translate("MainWindow", "The union of filters"))

        self.plotText.setText(_translate("MainWindow", "Example figure display area"))

        self.bait.setText( "AT4G39400")
        self.SD.setText("1")
        self.pValue.setText("0.05")


class PyQtMainEntry(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        folder = os.getcwd() + '\\output\\'
        if not os.path.exists(folder):
               os.mkdir(folder)
        shutil.rmtree(folder)
        os.mkdir(folder)


    def openFile(self):
        folder = os.getcwd() + '\\output\\'
        if not os.path.exists(folder):
               os.mkdir(folder)
        shutil.rmtree(folder)
        os.mkdir(folder)
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            QtCore.QDir.homePath(),
            'Text Files (*.txt) ;;All Files (*)',
            'Text Files (*.txt)',
            QtWidgets.QFileDialog.DontUseNativeDialog |
            QtWidgets.QFileDialog.DontResolveSymlinks
        )

        if filename:
            try:
                with open(filename) as fh:
                    out = open("output/data.txt", "w")
                    out.write(fh.read())
                    out.close()
                    self.Result.clear()
                    self.Result.setText("The file is loaded! Press 'show' to check it out! ")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")

    def showfile(self):
        try:
            self.Result.clear()
            t = open("output/data.txt", "r")
            self.Result.setText(t.read())
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")



    def withbait(self):
        df = pd.read_table("output/data.txt", header=[0, 1], index_col=0)
        bait_ID = self.bait.toPlainText()

        def ScaleOnBait(self):
            bait = self.loc[bait_ID]
            scaled_self = self.drop(index=bait_ID, axis=0) - bait
            scaled_self.to_csv('output/withbait_data.txt', sep='\t')

        ScaleOnBait(df)
        self.Result.clear()
        self.Result.setText("It's finished! Press 'show' to check it out!")


    def showbait(self):
        w = self.baitBox.currentText()

        try:
            self.Result.clear()
            if (w == "Yes"):
               t = open('output/withbait_data.txt', "r")
            if (w == "No"):
                t = open('output/data.txt', "r")
            self.Result.setText(t.read())
            self.plot.setPixmap(QtGui.QPixmap(""))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")

########################################################################################################
    def filter(self):

        w = self.baitBox.currentText()
        bait_ID = self.bait.toPlainText()

        p = open("output/paramet.txt", "a")
        p.write( w + " with Bait: " + bait_ID )
        p.write("\n")

        df = pd.read_table('output/data.txt', header=[0, 1], index_col=0)
        def ScaleOnBait(self):
            bait = self.loc[bait_ID]
            scaled_self = self.drop(index=bait_ID, axis=0) - bait
            return (scaled_self)

        if (w == "Yes"):
            d = ScaleOnBait(df)
        if (w == "No"):
            d = pd.read_table('output/data.txt', header=[0, 1], index_col=0)

        def sort(self):
            group_mean = self.mean(axis=1, level=0)
            experiments = self.columns.get_level_values(0).unique()
            control = experiments[0]

            Filter_C = group_mean[group_mean.iloc[:, 0].isna()].dropna(how='all')
            FilterC = pd.DataFrame()
            for exp in experiments[1:]:
                FilterC["log2 FC " + exp + "-" + control] = Filter_C[exp].map(lambda x: np.nan if np.isnan(x) else 1)
            FilterC = FilterC.reset_index().rename(columns={'index': 'Preys'})
            FilterC.insert(loc=0, column='Receptors_Baits', value=bait_ID)

            FilterC.fillna('NA').to_csv('output/DEPs_FilterA.txt', sep='\t', index=False)

        sort(d)
        self.Result.clear()
        self.Result.setText("it's finished! All results exist in /output")


    def showfilter(self):
        try:

            t = open("output/DEPs_FilterA.txt", "r")
            self.Result.setText(t.read())
            self.plot.setPixmap(QtGui.QPixmap(""))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")

##############################################################################################################################


    def mean_std(self):
        fold_std = float(self.SD.toPlainText())
        w = self.baitBox.currentText()
        bait_ID = self.bait.toPlainText()
        df = pd.read_table('output/data.txt', header=[0, 1], index_col=0)

        p = open("output/paramet.txt", "a")
        p.write( "sd: " + self.SD.toPlainText())
        p.write("\n")


        def ScaleOnBait(self):
            bait = self.loc[bait_ID]
            scaled_self = self.drop(index=bait_ID, axis=0) - bait
            return (scaled_self)

        if (w == "Yes"):
            d = ScaleOnBait(df)

        if (w == "No"):
            d = pd.read_table('output/data.txt', header=[0, 1], index_col=0)


        def mean(self):
            #### Calculate the mean values for each group, check if the values are in normal distribution using violinplot
            group_mean = self.mean(axis=1, level=0)
            group_mean.to_csv('output/mean_LFQ_for_biological_replicates.txt', sep='\t')
            plt.figure()
            sns.set_style('white')
            dfplot1 = group_mean.unstack().reset_index().rename(
                columns={'level_0': 'experiment', 0: 'mean value of replicates'})
            sns.violinplot(data=dfplot1, x="experiment", y="mean value of replicates", linewidth=.5, palette='husl',
                           saturation=1)
            plt.grid(axis='y', linestyle='-.', linewidth=0.5, color='grey')
            plt.savefig('output/violinplot_group_mean.png')

            experiments = self.columns.get_level_values(0).unique()
            control = experiments[0]
            fc_data = pd.DataFrame()
            log2fc = pd.DataFrame()
            for exp in experiments[1:]:
                log2fc[exp + "-" + control] = group_mean[exp] - group_mean[control]

            fc_data = log2fc
            fc_data = fc_data.reset_index().rename(columns={'index': 'Preys'})
            fc_data.insert(loc=0, column='Receptors_Baits', value=bait_ID)
            fc_data.to_csv('output/log2FC_data.txt', sep='\t', index=False)

            FC_means, f_stds = log2fc.describe().loc['mean'], log2fc.describe().loc['std'] * fold_std
            up, down = FC_means + f_stds, FC_means - f_stds

            FilterA = pd.DataFrame()
            for exp, u, d in zip(experiments[1:], up, down):
                FilterA["log2 FC " + exp + "-" + control] = \
                log2fc[(log2fc[exp + "-" + control] > u) | (log2fc[exp + "-" + control] < d)][exp + "-" + control]
            FilterA = FilterA.reset_index().rename(columns={'index': 'Preys'})
            FilterA.insert(loc=0, column='Receptors_Baits', value=bait_ID)
            FilterA.fillna('NA').to_csv('output/DEPs_FilterB.txt', sep='\t', index=False)
            plt.figure()
            dfplot2 = log2fc.unstack().reset_index().rename(columns={'level_0': 'treatment-control', 0: 'log2 FC'})
            sns.violinplot(data=dfplot2, x="treatment-control", y="log2 FC", linewidth=.3, palette='husl')
            for i, mean, fstd in zip(range(len(FC_means)), FC_means, f_stds):
                plt.hlines(y=mean, xmin=i - 0.3, xmax=i + 0.3, colors='black', linewidth=.5)
                plt.hlines(y=mean + fstd, xmin=i - 0.2, xmax=i + 0.2, colors='black', linewidth=.5)
                plt.hlines(y=mean - fstd, xmin=i - 0.2, xmax=i + 0.2, colors='black', linewidth=.5)
            plt.savefig('output/violinplot_log2FC.png')


        mean(d)
        self.Result.clear()
        self.Result.setText("it's finished! All results exist in /output")


    def show_meansd(self):
        try:
            self.Result.clear()
            t = open("output/DEPs_FilterB.txt", "r")
            self.Result.setText(t.read())
            self.plot.setPixmap(QtGui.QPixmap("output/violinplot_log2FC.png"))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")
################################################################################################
    def ttest(self):

        w = self.baitBox.currentText()
        m = self.Methode3.currentText()
        sigmethod = self.Methode.currentText()
        cutp = float(self.pValue.toPlainText())
        bait_ID = self.bait.toPlainText()
        df = pd.read_table('output/data.txt', header=[0, 1], index_col=0)

        p = open("output/paramet.txt", "a")
        p.write(" methode: " + m)
        p.write("\n")
        p.write(" sigmethod: " + sigmethod)
        p.write("\n")
        p.write("p/f< " + self.pValue.toPlainText())
        p.write("\n")

        def ScaleOnBait(self):
            bait = self.loc[bait_ID]
            scaled_self = self.drop(index=bait_ID, axis=0) - bait
            return (scaled_self)

        if (w == "Yes"):
            d = ScaleOnBait(df)

        if (w == "No"):
            d = pd.read_table('output/data.txt', header=[0, 1], index_col=0)

        if (m == "Student's t-test"):
            v = True

        if (m == "Welch's t-test"):
            v = False



        def tt(self):
            ##### equal_var If True (default), perform a standard independent 2 sample test that assumes equal population variances.
            ##### 'sigmethod' is optional that using "p-value" or "fdr_bh" as the cut off value to define DEPs. Default is using "p-value".
            index, experiments = self.index, self.columns.get_level_values(0).unique()
            self = self.reset_index(drop=True)
            control = experiments[0]
            values = []
            for exp in experiments[1:]:
                ##### calculate p value of student t test
                exp_ps = pd.Series(stats.ttest_ind(self[control], self[exp], equal_var=v, axis=1)[1],
                                   name=(exp + "-" + control, "p-value"))
                values.append(exp_ps)
                ##### calculate fdr value using BH method
                uncorrected_ps, fdr_index = exp_ps.dropna().values, exp_ps.dropna().index
                values.append(pd.Series(multipletests(uncorrected_ps, method='fdr_bh')[1], index=fdr_index,
                                        name=(exp + "-" + control, "fdr_bh")))
                #### calculate fold change
                values.append(pd.Series(self[exp].mean(axis=1) - self[control].mean(axis=1),
                                        name=(exp + "-" + control, "log2 FC")))
                values.append(
                    pd.Series(exp_ps.map(lambda x: -np.log10(x)), name=(exp + "-" + control, " -log10 p-value")))
            results = pd.concat(values, axis=1).set_index(index)
            results.dropna(how='all').fillna('NA').to_csv('output/t-test_log2FC.txt', sep='\t')
            ##### define DEPs and drawing volcano plots
            compares = [exp + "-" + experiments[0] for exp in experiments[1:]]
            FilterB_values = []
            for cp in compares:
                FilterB_values.append(
                    pd.Series(results[results[cp][sigmethod] < cutp][cp]['log2 FC'], name="log2 FC " + cp))
            FilterB = pd.concat(FilterB_values, axis=1).reset_index().rename(columns={'index': 'Preys'})
            FilterB.insert(loc=0, column='Receptors_Baits', value=bait_ID)
            FilterB.to_csv("output/DEPs_FilterC.txt", sep='\t', index=False)
            for cp in compares:
                plt.figure()
                sns.set_style('whitegrid')
                subtable = results[cp].dropna(how='any')
                subtable['regulation'] = subtable.apply(
                    lambda x: 'up' if ((x[sigmethod] < cutp) & (x['log2 FC'] > 0)) else 'down' if (
                                (x[sigmethod] < cutp) & (x['log2 FC'] < 0)) else 'not regulated', axis=1)
                sns.scatterplot(data=subtable, x='log2 FC', y=' -log10 p-value', hue='regulation',
                                hue_order=['up', 'down', 'not regulated'], palette=['red', 'blue', 'grey'])
                plt.title(cp)
                plt.savefig("output/VolcanoPlot_" + cp + ".png")
                plt.savefig("output/VolcanoPlot1.png")
        tt(d)
        self.Result.clear()
        self.Result.setText("it's finished! All results exist in /output")



    def ShowT(self):
        try:
            self.Result.clear()
            t = open("output/t-test_log2FC.txt", "r")
            self.Result.setText(t.read())
            self.plot.setPixmap(QtGui.QPixmap("output/VolcanoPlot1.png"))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")
###############################################################################################
    def vennTest(self):
        def myvenn(fa, fb, fc):
            setnames = [x for x in fa.columns if 'log2 FC' in x]
            fig = plt.figure()
            for i, name in enumerate(setnames):
                ax = fig.add_subplot(int("33" + str(i + 1)))
                sname = name.strip("log2 FC").split("-")[0]
                setcollect = {}
                for fname, filter in zip(['FilterA', 'FilterB', 'FilterC'], [fa, fb, fc]):
                    f = filter.set_index('Preys')
                    setcollect[sname + " " + fname] = set(f[~(f[name].isna())][name].index)
                venn(setcollect, ax=ax, fontsize=6)
                plt.tight_layout()
                plt.savefig("output/VennFilters" + sname + ".png")
            plt.savefig("output/VennFilters.png")
            plt.savefig("output/VennFilters.pdf")
            plt.savefig("output/VennFilters.png")



        filterA, filterB, filterC = [pd.read_table(x) for x in
                                         ["output/DEPs_FilterA.txt", "output/DEPs_FilterB.txt",
                                          "output/DEPs_FilterC.txt"]]



        myvenn(filterA, filterB, filterC)
        DEPs = pd.concat([filterA, filterB, filterC], axis=0)
        DEPs.fillna('NA').to_csv('output/DEPs_All.txt', sep='\t', index=False)
        DEPs.fillna('NA').to_csv('output/DEPs_All.txt', sep='\t', index=False)
        self.Result.clear()
        self.Result.setText("it's finished! All results exist in /output")


    def ShowV(self):
        try:
            self.Result.clear()
            t = open("output/DEPs_All.txt", "r")
            self.Result.setText(t.read())
            self.plot.setPixmap(QtGui.QPixmap("output/VennFilters.png"))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()

    sys.exit(app.exec_())