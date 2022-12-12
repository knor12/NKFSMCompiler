#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTextEdit>
#include <QTimer>
#include "TraficLightFSM.h"
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();


    void setTextBoxBackColor(QTextEdit * txt, QColor color );
    void setColorTxtRedL2( QColor color);
    void setColorTxtRedL1( QColor color);

    void stopTimers();
    void startTimers();

    void restartTimerOnStateChange();

public slots:

    void handler_timer100s();
    void handler_timer10s();
    void handler_timer1s();
    void handler_timer2s();
    void handler_timer3s();




private slots:
    void on_btnOn_clicked();

    void on_btnOff_clicked();

private:
    Ui::MainWindow *ui;
    QTimer *timer100s;
    QTimer *timer10s;
    QTimer *timer1s;
    QTimer *timer2s;
    QTimer *timer3s;

    struct TraficLightFSM fsm;
};

#endif // MAINWINDOW_H
