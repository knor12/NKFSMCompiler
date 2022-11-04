
#include <stdint.h>
#include "GenericTimer.h"




static QDateTime  startup ;
int  GenericTimer_Init( void )
{

    startup = QDateTime::currentDateTime();

    return 0;
}



uint32_t GenericTimer_GetTicksMs()
{
    QDateTime now = QDateTime::currentDateTime();
    uint32_t diff =startup.msecsTo(now);
    return diff;

}

uint32_t GenericTimer_GetTicksSince(uint32_t ticks_)
{
    uint32_t nowms = GenericTimer_GetTicksMs();
    return nowms-ticks_;

}

