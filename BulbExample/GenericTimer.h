
#ifndef GENERICTIMER_H_
#define GENERICTIMER_H_

//#ifdef __cplusplus
//extern "C"
//{
//#endif		/* __cplusplus */

#include <stdint.h>
#include <QDateTime.h>


int GenericTimer_Init(void);


uint32_t GenericTimer_GetTicksMs(void);


uint32_t GenericTimer_GetTicksSince(uint32_t ticks_);

//#ifdef __cplusplus
//}
//#endif		/* __cplusplus */
#endif /* GENERICTIMER_H_ */
