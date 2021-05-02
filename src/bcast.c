#include <stdio.h>

int MPI_Bcast(int a)
{
    printf("This is %s\n", __func__);
    return 0;
}
