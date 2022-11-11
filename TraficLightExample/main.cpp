

#include <QApplication>
#include <QThread>

#include  "TraficLightFSM.h"
#include "GenericTimer.h"



#define timeOut100_ (1)
#define on_ (2)
#define off_ (3)
#define timeOut1_ (4)
#define timeOut10_ (5)
#define timeOut2_ (6)
#define  timeOut3_ (7)
uint32_t evets[] = {timeOut100_, on_, timeOut1_, timeOut2_, timeOut3_,timeOut2_, timeOut100_, on_ , off_};


uint32_t timeOut500;
uint32_t timeOut1000;

#define TIMEOUT_ARM(T) {T = GenericTimer_GetTicksMs(); }
#define TIMEOUT_CLEAR(T) {T =0; }
#define TIMEOUT_HAPPEND(T,X) ((GenericTimer_GetTicksSince(T)>(X)&& (T>0)) ?1:0)


/*if state change rearm all timeout counters for all states*/
/*FSM will not process timeouts where they are needed*/

TraficLightFSM light;

int main(int argc, char *argv[])
{

    TraficLightFSM_Init(&light);


    for(int i = 0; i< (sizeof(evets)/sizeof(evets[0])); i++)
    {
        printf("=================\n");
        switch(evets[i])
        {
        case timeOut100_ :
            TraficLightFSM_timeOut100(&light, (void*)0);
            break;
        case on_ :
            TraficLightFSM_on(&light, (void*)0);
            break;

        case off_ :
            TraficLightFSM_off(&light, (void*)0);
            break;
        case timeOut1_ :
            TraficLightFSM_timeOut1(&light, (void*)0);
            break;
        case timeOut10_ :
            TraficLightFSM_timeOut10(&light, (void*)0);
            break;
        case timeOut2_ :
            TraficLightFSM_timeOut2(&light, (void*)0);
            break;
        case timeOut3_ :
            TraficLightFSM_timeOut3(&light, (void*)0);
            break;
        }
    }

    return 0;
    GenericTimer_Init();
    TIMEOUT_ARM(timeOut500);
    TIMEOUT_ARM(timeOut1000);


    printf("hellowww \n \n \n");
    return 0;
}

