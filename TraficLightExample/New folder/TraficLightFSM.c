/*
*this file is auto generated by NKCompiler, do not edit manualy 
*@file TraficLightFSM.c
*@date 2022-11-08
*@author n.kessa
*@brief state machine TraficLightFSM FSM code
*/

#include "TraficLightFSM.h" 
#include "TraficLightGlue.h" 

#include <stdlib.h> 


#define MAX_NUM_STATES (13)


/*initialization function*/
void TraficLightFSM_Init(struct TraficLightFSM * fsm)
{
    fsm->state=init;
}

/*this function processes the event timeOut1 based on current state and conditions specified.*/
int TraficLightFSM_timeOut1(struct TraficLightFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Green_GreenOn)
    {
        ret=GreenOnExit(o);
        
        ret|=GreenOffEntry(o);
        if (ret >= 0)
        {
            fsm->state = Green_GreenOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
        ret|= TraficLightFSM_timeOut60(fsm,o);/*on exit rased event*/
                return ret;
    }
    

    
    if (fsm->state == Green_GreenOff)
    {
        ret=GreenOffExit(o);
        
        ret|=GreenOnEntry(o);
        if (ret >= 0)
        {
            fsm->state = Green_GreenOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
        ret|= TraficLightFSM_timeOut60(fsm,o);/*on exit rased event*/
                return ret;
    }
    

    
    if (fsm->state == Yellow_YellowOn)
    {
        ret=yellowOnExit(o);
        
        ret|=yellowOffEntry(o);
        if (ret >= 0)
        {
            fsm->state = Yellow_YellowOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Yellow_YellowOff)
    {
        ret=yellowOffExit(o);
        
        ret|=yellowOnEntry(o);
        if (ret >= 0)
        {
            fsm->state = Yellow_YellowOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                ret|= TraficLightFSM_timeOut1(fsm,o);/* on entry rased event*/
        return ret;
    }
    

    
    if (fsm->state == Red_redOff)
    {
        
        
        ret|=redOn(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Red_redOn)
    {
        ret=redOff(o);
        
        ret|=redOff(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Blue_blueOff)
    {
        
        
        ret|=blueOn(o);
        if (ret >= 0)
        {
            fsm->state = Blue_blueOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Blue_blueOn)
    {
        ret=blueOff(o);
        
        ret|=blueOff(o);
        if (ret >= 0)
        {
            fsm->state = Blue_blueOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Orange_orangeOff)
    {
        
        
        ret|=orangeOn(o);
        if (ret >= 0)
        {
            fsm->state = Orange_orangeOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Orange_orangeOn)
    {
        ret=orangeOff(o);
        
        ret|=orangeOff(o);
        if (ret >= 0)
        {
            fsm->state = Orange_orangeOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    
    return 0;
}


/*this function processes the event timeOut30 based on current state and conditions specified.*/
int TraficLightFSM_timeOut30(struct TraficLightFSM * fsm, void * o)
{

    int ret = 0; 

    
    if ((fsm->state == Green_GreenOn)/*going from green to Green_to_Yellow*/)
    {
        ret=GreenOnExit(o);
        
        ret|=green_to_yellow(o);
        if (ret >= 0)
        {
            fsm->state = Green_to_Yellow;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
        ret|= TraficLightFSM_timeOut60(fsm,o);/*on exit rased event*/
        ret|= TraficLightFSM_any(fsm,o);/* on entry rased event*/
        return ret;
    }
    

    
    if ((fsm->state == Green_GreenOff)/*going from green to Green_to_Yellow*/)
    {
        ret=GreenOffExit(o);
        
        ret|=green_to_yellow(o);
        if (ret >= 0)
        {
            fsm->state = Green_to_Yellow;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
        ret|= TraficLightFSM_timeOut60(fsm,o);/*on exit rased event*/
        ret|= TraficLightFSM_any(fsm,o);/* on entry rased event*/
        return ret;
    }
    
    return 0;
}


/*this function processes the event timeOut60 based on current state and conditions specified.*/
int TraficLightFSM_timeOut60(struct TraficLightFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Yellow_YellowOn)
    {
        ret=yellowOnExit(o);
        
        ret|=blueOff(o);
        if (ret >= 0)
        {
            fsm->state = Blue_blueOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Blue_blueOff)
    {
        
        
        ret|=orangeOff(o);
        if (ret >= 0)
        {
            fsm->state = Orange_orangeOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Orange_orangeOff)
    {
        
        
        ret|=redOff(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Yellow_YellowOff)
    {
        ret=yellowOffExit(o);
        
        ret|=blueOff(o);
        if (ret >= 0)
        {
            fsm->state = Blue_blueOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Blue_blueOn)
    {
        ret=blueOff(o);
        
        ret|=orangeOff(o);
        if (ret >= 0)
        {
            fsm->state = Orange_orangeOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Orange_orangeOn)
    {
        ret=orangeOff(o);
        
        ret|=redOff(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    
    return 0;
}


/*this function processes the event timeOut20 based on current state and conditions specified.*/
int TraficLightFSM_timeOut20(struct TraficLightFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Red_redOff)
    {
        
        
        ret|=GreenOnEntry(o);
        if (ret >= 0)
        {
            fsm->state = Green_GreenOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Red_redOn)
    {
        ret=redOff(o);
        
        ret|=GreenOnEntry(o);
        if (ret >= 0)
        {
            fsm->state = Green_GreenOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    
    return 0;
}


/*this function processes the event timeOut2 based on current state and conditions specified.*/
int TraficLightFSM_timeOut2(struct TraficLightFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Red_redOff)
    {
        
        
        ret|=redOff(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == init)
    {
        
        
        ret|=redOff(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Blue_blueOff)
    {
        
        
        ret|=blueOff(o);
        if (ret >= 0)
        {
            fsm->state = Blue_blueOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Orange_orangeOff)
    {
        
        
        ret|=orangeOff(o);
        if (ret >= 0)
        {
            fsm->state = Orange_orangeOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Red_redOn)
    {
        ret=redOff(o);
        
        ret|=redOff(o);
        if (ret >= 0)
        {
            fsm->state = Red_redOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Blue_blueOn)
    {
        ret=blueOff(o);
        
        ret|=blueOff(o);
        if (ret >= 0)
        {
            fsm->state = Blue_blueOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    

    
    if (fsm->state == Orange_orangeOn)
    {
        ret=orangeOff(o);
        
        ret|=orangeOff(o);
        if (ret >= 0)
        {
            fsm->state = Orange_orangeOff;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                        return ret;
    }
    
    return 0;
}


/*this function processes the event any based on current state and conditions specified.*/
int TraficLightFSM_any(struct TraficLightFSM * fsm, void * o)
{

    int ret = 0; 

    
    if (fsm->state == Green_to_Yellow)
    {
        
        
        ret|=yellowOnEntry(o);
        if (ret >= 0)
        {
            fsm->state = Yellow_YellowOn;
        }else 
        {
            fsm->state = TraficLight_Error_State;
        }
                ret|= TraficLightFSM_timeOut1(fsm,o);/* on entry rased event*/
        return ret;
    }
    
    return 0;
}
