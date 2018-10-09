#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSpacerItem>
#include <QMainWindow>
#include "streamer.h"
#include <QPushButton>
#include <QWidget>
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    streamer * stream;
    QVBoxLayout * verLay;
    QHBoxLayout * horLay;
    QSpacerItem * vSpacer;
    QPushButton * bttn1;
    QWidget * centralWidget;
};

#endif // MAINWINDOW_H
