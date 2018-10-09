#-------------------------------------------------
#
# Project created by QtCreator 2018-10-05T10:36:09
#
#-------------------------------------------------

QT       += core gui multimedia multimediawidgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = guia
TEMPLATE = app

PKGCONFIG += gstreamer-1.0 gstreamer-1.0-app
SOURCES += main.cpp\
        mainwindow.cpp \
    streamer.cpp

HEADERS  += mainwindow.h \
    streamer.h

FORMS    += mainwindow.ui
