#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QColorDialog>

#ifdef __cplusplus
extern "C"
{
#endif		/* __cplusplus */

int oInitWrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("oInit");

    return 0;

}


int iwarmUpWrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("oInit");
    return 0;

}
int oLightOffWrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("oLightOff");
    QColor color =Qt::gray;
    w->setColorTxtRedL1(color);
    w->setColorTxtRedL2(color);
    return 0;

}
int iInitWrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("iInit");
    return 0;

}
int iRedOnL1Wrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("iRedOnL1");
    QColor color = Qt::red;
    w->setColorTxtRedL1(color);
    return 0;

}
int oRedOnL1Wrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    QColor color =Qt::gray;
    w->setColorTxtRedL1(color);
    //w->setColorTxtRedL2(color);
    w->setWindowTitle("oRedOnL1");
    return 0;

}
int iLightOffWrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("iLightOff");
    QColor color = Qt::gray;
    w->setColorTxtRedL1(color);
    w->setColorTxtRedL2(color);
    return 0;

}
int iRedOnL2Wrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("iRedOnL2");
    QColor color =Qt::red;
    //w->setColorTxtRedL1(color);
    w->setColorTxtRedL2(color);
    return 0;

}
int oRedOnL2Wrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    QColor color =Qt::gray;
    //w->setColorTxtRedL1(color);
    w->setColorTxtRedL2(color);
    w->setWindowTitle("oRedOnL2");
    return 0;

}
int owarmUpWrapper(void * o)
{

    MainWindow *w = (MainWindow *)(o);
    w->setWindowTitle("oInit");
    return 0;

}

#ifdef __cplusplus
}
#endif		/* __cplusplus */


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);


    timer100s = new QTimer(this);
    timer10s = new QTimer(this);
    timer1s = new QTimer(this);
    timer2s = new QTimer(this);
    timer3s = new QTimer(this);

    connect(timer100s, &QTimer::timeout, this, &MainWindow::handler_timer100s);
    connect(timer10s, &QTimer::timeout, this, &MainWindow::handler_timer10s);
    connect(timer1s, &QTimer::timeout, this, &MainWindow::handler_timer1s);
    connect(timer2s, &QTimer::timeout, this, &MainWindow::handler_timer2s);
    connect(timer3s, &QTimer::timeout, this, &MainWindow::handler_timer3s);


    TraficLightFSM_Init(&fsm);

}




MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setTextBoxBackColor(QTextEdit * txt, QColor color)
{
    //QColor color = QColorDialog::getColor(Qt::white,this);
    QPalette palette;
    palette.setColor(QPalette::Base,color);
    if(color.isValid())
        txt->setPalette(palette);
}

void MainWindow::setColorTxtRedL2(QColor color)
{
    this->setTextBoxBackColor(ui->txtRedL2, color);
}

void MainWindow::setColorTxtRedL1(QColor color)
{
    this->setTextBoxBackColor(ui->txtRedL1, color);
}

void MainWindow::stopTimers()
{
    timer100s->stop();
    timer10s->stop();
    timer1s->stop();
    timer2s->stop();
    timer3s->stop();
}

void MainWindow::startTimers()
{
    timer100s->start(100*000);
    timer10s->start(10*1000);
    timer1s->start(1*1000);
    timer2s->start(2*1000);
    timer3s->start(3*1000);
}

void MainWindow::handler_timer100s()
{
    FSMTraficLight_State_t old =  fsm.state;

    TraficLightFSM_timeOut100(&fsm, this);

    if (old !=fsm.state)
    {
        this->stopTimers();
        this->startTimers();
    }

}

void MainWindow::handler_timer10s()
{
    FSMTraficLight_State_t old =  fsm.state;
    TraficLightFSM_timeOut10(&fsm, this);
    if (old !=fsm.state)
    {
        this->timer10s->stop();
        this->timer10s->start();
    }
}

void MainWindow::handler_timer1s()
{
    FSMTraficLight_State_t old =  fsm.state;
    TraficLightFSM_timeOut1(&fsm, this);
    if (old !=fsm.state)
    {
        this->timer1s->stop();
        this->timer1s->start();
        this->timer2s->stop();
        this->timer2s->start();
        this->timer3s->stop();
        this->timer3s->start();
    }
}

void MainWindow::handler_timer2s()
{
    FSMTraficLight_State_t old =  fsm.state;
    TraficLightFSM_timeOut2(&fsm, this);
    if (old !=fsm.state)
    {
        this->timer1s->stop();
        this->timer1s->start();
        this->timer2s->stop();
        this->timer2s->start();
        this->timer3s->stop();
        this->timer3s->start();
    }
}

void MainWindow::handler_timer3s()
{
    FSMTraficLight_State_t old =  fsm.state;
    TraficLightFSM_timeOut3(&fsm, this);
    if (old !=fsm.state)
    {
        this->timer1s->stop();
        this->timer1s->start();
        this->timer2s->stop();
        this->timer2s->start();
        this->timer3s->stop();
        this->timer3s->start();
    }
}

void MainWindow::on_btnOn_clicked()
{
    FSMTraficLight_State_t old =  fsm.state;
    TraficLightFSM_on(&fsm, this);
    if (old !=fsm.state)
    {
        this->stopTimers();
        this->startTimers();
    }
}


void MainWindow::on_btnOff_clicked()
{
    FSMTraficLight_State_t old =  fsm.state;
    TraficLightFSM_off(&fsm, this);
    this->stopTimers();
    if (old !=fsm.state)
    {
        this->stopTimers();
        this->startTimers();
    }
}

