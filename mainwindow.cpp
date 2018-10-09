#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{

    ui->setupUi(this);
    /*
     * WebCam Moodule
     *
    this->setGeometry(200,200,800,600);
    verLay=new QVBoxLayout();
    centralWidget=new QWidget;
    centralWidget->setLayout(verLay);
    stream=new streamer(centralWidget);
    verLay->addWidget(stream->getViewFinder());
    verLay->setMargin(0);
    bttn1=new QPushButton(this);
    bttn1->setText("Useless");
    verLay->addWidget(bttn1);
    this->setCentralWidget(centralWidget);
*/

    /*
    LocalVideo Moduel
  */
    this->setGeometry(200,200,800,600);
    verLay=new QVBoxLayout();
    centralWidget=new QWidget;
    centralWidget->setLayout(verLay);
    stream=new streamer(centralWidget);
    verLay->addWidget(stream->getVideoWidget());
    verLay->setMargin(0);
    bttn1=new QPushButton(this);
    bttn1->setText("Useless");
    verLay->addWidget(bttn1);
    this->setCentralWidget(centralWidget);


}

MainWindow::~MainWindow()
{
    delete ui;
}

/*
//aren't supported :

//supported : wmv ,avi,mkv,mp4,flv,mpg,3gp

*/
