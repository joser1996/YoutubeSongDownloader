#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->downloadButton, &QPushButton::clicked, this, &MainWindow::beginDownload);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::beginDownload() {
    qDebug() << "Starting download for: " << ui->urlTextEdit->text();
}
