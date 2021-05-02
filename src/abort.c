#include <stdio.h>

int MPI_Abort(int a)
{
    printf("This is %s\n", __func__);
    return 0;
}
