/*
*this file is auto generated by NKCompiler, do not edit manualy 
*@file BulbFSM.c
*@date 2022-10-27
*@author n.kessa
*@brief state machine BulbFSM FSM code
*/

#include "BulbFSM.h" 
#include "BulbGlue.h" 

#include <stdlib.h> 


#define MAX_NUM_STATES (4)


/*initialization function*/
void BulbFSM_Init(struct BulbFSM * fsm)
{
    fsm->state=Level0;
}

int BulbFSM_Up(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 
    if (fsm->state == Level0)
    {
        ret = Level1Handler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level1;
            return ret;
        }
    }
    
    if (fsm->state == Level1)
    {
        ret = Level2Handler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level2;
            return ret;
        }
    }
    
    if (fsm->state == Level2)
    {
        ret = Level2Handler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level2;
            return ret;
        }
    }
    
    return 0;}


int BulbFSM_Down(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 
    if (fsm->state == Level0)
    {
        ret = Level0Handler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level0;
            return ret;
        }
    }
    
    if (fsm->state == Level1)
    {
        ret = Level0Handler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level0;
            return ret;
        }
    }
    
    if (fsm->state == Level2)
    {
        ret = Level1Handler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level1;
            return ret;
        }
    }
    
    return 0;}


int BulbFSM_Error(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 
    if (fsm->state == Level0)
    {
        ret = ErrorHandler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Error_st;
            return ret;
        }
    }
    
    if (fsm->state == Level1)
    {
        ret = ErrorHandler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Error_st;
            return ret;
        }
    }
    
    if (fsm->state == Level2)
    {
        ret = ErrorHandler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Error_st;
            return ret;
        }
    }
    
    return 0;}


int BulbFSM_reset(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 
    if (fsm->state == Error_st)
    {
        ret = ResetHandler(o);
        if (ret < 0)
        {
            fsm->state = Error_st;
            return ret;
        }else 
        {
            fsm->state = Level0;
            return ret;
        }
    }
    
    return 0;}
