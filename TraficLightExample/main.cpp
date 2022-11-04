

#include <QApplication>
#include <QThread>

#include  "TraficLightFSM.h"
#include "GenericTimer.h"



#define timeOut1_ (1)
#define timeOut30_ (2)
#define timeOut60_ (3)
#define noEvent_ (4)
#define timeOut20_ (5)
#define timeOut2_ (6)
uint32_t evets[] = {timeOut2_,timeOut2_,timeOut2_,timeOut2_, timeOut1_,
                    timeOut20_,
                    timeOut1_,timeOut1_,timeOut1_,timeOut1_,timeOut1_,timeOut1_,timeOut1_,
                    timeOut30_,timeOut30_,
                   timeOut1_,timeOut1_,timeOut1_,timeOut1_,timeOut1_,
                   timeOut60_,timeOut2_};


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
        switch(evets[i])
        {
        case timeOut1_ :
            TraficLightFSM_timeOut1(&light, (void*)0);
            break;
        case timeOut30_ :
            TraficLightFSM_timeOut30(&light, (void*)0);
            break;

        case timeOut60_ :
            TraficLightFSM_timeOut60(&light, (void*)0);
            break;
        case timeOut20_ :
            TraficLightFSM_timeOut20(&light, (void*)0);
            break;
        case timeOut2_ :
            TraficLightFSM_timeOut2(&light, (void*)0);
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

