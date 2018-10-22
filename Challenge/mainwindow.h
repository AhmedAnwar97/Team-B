
#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSpacerItem>
#include <QMainWindow>
#include "streamer.h"
#include <QWidget>
#include "joystick.h"
#include <QPushButton>
#include "tcpsocket.h"
#include "udpsocket.h"
#include "gstream.h"
#include <QSignalMapper>
#include <QtDebug>
#include <QTimer>

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
//    streamer * stream;
    QVBoxLayout * verLay;
    QHBoxLayout * horLay;
    QSpacerItem * vSpacer;
    QPushButton * bttn1;
    QWidget * centralWidget;
    joystick * controller;
    QPushButton * bttnPrint;
    tcpsocket * piSock;
//    tcpsocket * ImageProcessingSock;
    gstream * str;
    QWidget * streamingWidget;

};

#endif // MAINWINDOW_H
