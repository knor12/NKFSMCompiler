/*
*this file is auto generated by NKCompiler, do not edit manualy
*@file BulbFSM.h
*@date 2022-11-03
*@author n.kessa
*@brief state machine BulbFSM FSM code
*/


#ifndef  BulbFSM_H
#define  BulbFSM_H


#ifdef __cplusplus 
extern "C" 
{ 
#endif		/* __cplusplus */ 
/*definition of all states*/
typedef enum 
{
    Level0,
    Level1,
    Error_st,
    Level2,
    Level3,
    Level4,
    Level5,
    Level6,
    Level7,
    Level8,
}FSMBulb_State_t;



/*definition of all events*/
typedef enum 
{
    Up,
    Down,
    Error,
    TimeOut500,
    TimeOut1000,
    reset,
    SomeEvent,
}FSMBulb_event_t;


/*definition of state structure*/
struct BulbFSM 
{
   FSMBulb_State_t state;
};
/*initialization function*/
void BulbFSM_Init(struct BulbFSM * fsm);


/*events*/
int BulbFSM_Up(struct BulbFSM * fsm, void * o);
int BulbFSM_Down(struct BulbFSM * fsm, void * o);
int BulbFSM_Error(struct BulbFSM * fsm, void * o);
int BulbFSM_TimeOut500(struct BulbFSM * fsm, void * o);
int BulbFSM_TimeOut1000(struct BulbFSM * fsm, void * o);
int BulbFSM_reset(struct BulbFSM * fsm, void * o);
int BulbFSM_SomeEvent(struct BulbFSM * fsm, void * o);

#ifdef __cplusplus
}
#endif		/* __cplusplus */
#endif /*BulbFSM_H*/