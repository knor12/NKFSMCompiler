

#include <QApplication>
#include <QThread>

#include  "bulbFSM.h"
#include "GenericTimer.h"

#define up (1)
#define down (2)
#define error (3)
#define noEvent (4)
#define reset (5)
uint32_t evets[] = {up, up, up, down, down, up, error,error,down, down, up,reset, down, down, up, up, up,up};


uint32_t timeOut500;
uint32_t timeOut1000;

#define TIMEOUT_ARM(T) {T = GenericTimer_GetTicksMs(); }
#define TIMEOUT_CLEAR(T) {T =0; }
#define TIMEOUT_HAPPEND(T,X) ((GenericTimer_GetTicksSince(T)>(X)&& (T>0)) ?1:0)


/*if state change rearm all timeout counters for all states*/
/*FSM will not process timeouts where they are needed*/

BulbFSM bulb;
char strUp[] = "Up";
char strDown[] = "Down";
char strError[] = "Error";
int main(int argc, char *argv[])
{

    BulbFSM_Init(&bulb);


    for(int i = 0; i< (sizeof(evets)/sizeof(evets[0])); i++)
    {
        switch(evets[i])
        {
        case up :
            BulbFSM_Up(&bulb, (void*)strUp);
            break;
        case down :
            BulbFSM_Down(&bulb, (void*)strDown);
            break;

        case error :
            BulbFSM_Error(&bulb, (void*)strError);
            break;
        case reset :
            BulbFSM_reset(&bulb, (void*)strError);
            break;
        }
    }

    //return 0;
    GenericTimer_Init();
    TIMEOUT_ARM(timeOut500);
    TIMEOUT_ARM(timeOut1000);

    int i =10;
    while(i)
    {
        QCoreApplication::processEvents();
        //QThread::msleep(100);
        //printf(".");
        if (TIMEOUT_HAPPEND(timeOut500, 250))
        {
            TIMEOUT_ARM(timeOut500);
            BulbFSM_TimeOut500(&bulb, (void*)strError);
            i--;
        }



        if (TIMEOUT_HAPPEND(timeOut1000, 1000))
        {
            TIMEOUT_ARM(timeOut1000);
            BulbFSM_TimeOut1000(&bulb, (void*)strError);
            i--;
        }

    }

    printf("hellowww \n \n \n");
    return 0;
}

