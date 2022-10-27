

#include <QApplication>
#include  "bulbFSM.h"

#define up (1)
#define down (2)
#define error (3)
#define noEvent (4)
#define reset (5)
uint32_t evets[] = {up, up, up, down, down, up, error,reset, down, down, up, up, up};

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

    printf("hellowww \n \n \n");
    return 0;
}

