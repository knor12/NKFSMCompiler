/*
*this file is auto generated by NKCompiler, do not edit manualy 
*@file BulbFSM.c
*@date 2022-11-03
*@author n.kessa
*@brief state machine BulbFSM FSM code
*/

#include "BulbFSM.h" 
#include "BulbGlue.h" 

#include <stdlib.h> 


#define MAX_NUM_STATES (10)


/*initialization function*/
void BulbFSM_Init(struct BulbFSM * fsm)
{
    fsm->state=Level0;
}

/*this function processes the event Up based on current state and conditions specified.*/
int BulbFSM_Up(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    /*if up event and in Level0 go to Level1*/
    if (fsm->state == Level0)
    {
        ret=onExitLevel0(o);
        
        ret|=onEnterLevel1(o);
        if (ret >= 0)
        {
            fsm->state = Level1;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level1)
    {
        ret=onExitLevel1(o);
        ret|=Level2Handler(o);
        ret|=onEnterLevel2(o);
        if (ret >= 0)
        {
            fsm->state = Level2;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    /*this should never transition. an example what you can do with conditions to influence the FSM behavior*/
    if ((fsm->state == Level2)&&(0))
    {
        
        ret|=Level2Handler(o);
        
        if (ret >= 0)
        {
            fsm->state = Level2;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    uint32_t * arg = (uint32_t*)o ;/*only if proper conditions are met*/
    if ((fsm->state == Level2)&& (*(arg+1) ==10))
    {
        ret=onExitLevel2(o);
        ret|=incrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level3;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level3)
    {
        
        ret|=incrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level4;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level4)
    {
        
        ret|=incrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level5;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level5)
    {
        
        ret|=incrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level6;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level6)
    {
        
        ret|=incrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level7;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level7)
    {
        
        ret|=noOp_(o);
        
        if (ret >= 0)
        {
            fsm->state = Level7;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Error_st)
    {
        
        ret|=ErrorHandlerUp(o);
        
        if (ret >= 0)
        {
            fsm->state = Error_st;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}


/*this function processes the event Down based on current state and conditions specified.*/
int BulbFSM_Down(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Level0)
    {
        
        ret|=Level0Handler(o);
        
        if (ret >= 0)
        {
            fsm->state = Level0;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    /*some random comment for this transition*/
    if (fsm->state == Level1)
    {
        ret=onExitLevel1(o);
        ret|=Level0Handler(o);
        ret|=onEnterLevel0(o);
        if (ret >= 0)
        {
            fsm->state = Level0;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if ((fsm->state == Level2)&&(100*2!=200))
    {
        ret=onExitLevel2(o);
        ret|=Level1Handler(o);
        ret|=onEnterLevel1(o);
        if (ret >= 0)
        {
            fsm->state = Level1;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if ((fsm->state == Level2)&&(100*2==200))
    {
        ret=onExitLevel2(o);
        ret|=Level0Handler(o);
        ret|=onEnterLevel0(o);
        if (ret >= 0)
        {
            fsm->state = Level0;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level2)
    {
        ret=onExitLevel2(o);
        ret|=decrementLevel(o);
        ret|=onEnterLevel1(o);
        if (ret >= 0)
        {
            fsm->state = Level1;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level3)
    {
        
        ret|=decrementLevel(o);
        ret|=onEnterLevel2(o);
        if (ret >= 0)
        {
            fsm->state = Level2;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level4)
    {
        
        ret|=decrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level3;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level5)
    {
        
        ret|=decrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level4;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level6)
    {
        
        ret|=decrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level5;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level7)
    {
        
        ret|=decrementLevel(o);
        
        if (ret >= 0)
        {
            fsm->state = Level6;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Error_st)
    {
        
        ret|=ErrorHandlerDown(o);
        
        if (ret >= 0)
        {
            fsm->state = Error_st;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}


/*this function processes the event Error based on current state and conditions specified.*/
int BulbFSM_Error(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    /*condition to process  event from any state*/
    if ((fsm->state == Level0)||(1==1))
    {
        ret=onExitLevel0(o);
        ret|=ErrorHandler(o);
        ret|=onEnterError(o);
        if (ret >= 0)
        {
            fsm->state = Error_st;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}


/*this function processes the event TimeOut500 based on current state and conditions specified.*/
int BulbFSM_TimeOut500(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Level2)
    {
        
        ret|=Level2TimeOut500Handler(o);
        
        if (ret >= 0)
        {
            fsm->state = Level2;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}


/*this function processes the event TimeOut1000 based on current state and conditions specified.*/
int BulbFSM_TimeOut1000(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Level2)
    {
        
        ret|=Level2TimeOut1000Handler(o);
        
        if (ret >= 0)
        {
            fsm->state = Level2;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}


/*this function processes the event reset based on current state and conditions specified.*/
int BulbFSM_reset(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Error_st)
    {
        
        ret|=ResetHandler(o);
        ret|=onEnterLevel0(o);
        if (ret >= 0)
        {
            fsm->state = Level0;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}


/*this function processes the event SomeEvent based on current state and conditions specified.*/
int BulbFSM_SomeEvent(struct BulbFSM * fsm, void * o)
{

    int ret = 0; 

    (void)o;/*example transaction that does nothing */
    if (fsm->state == Level8)
    {
        
        
        
        if (ret >= 0)
        {
            fsm->state = Level8;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level8)
    {
        
        
        
        if (ret >= 0)
        {
            fsm->state = Level8;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level8)
    {
        
        
        
        if (ret >= 0)
        {
            fsm->state = Level8;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level8)
    {
        
        
        
        if (ret >= 0)
        {
            fsm->state = Level8;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    

    
    if (fsm->state == Level8)
    {
        
        ret|=newHandler(o);
        
        if (ret >= 0)
        {
            fsm->state = Level8;
        }else 
        {
            fsm->state = Error_st;
        }
        return ret;
    }
    
    return 0;
}
