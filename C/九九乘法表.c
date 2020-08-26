/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int j;

	i=1;
	while(i<=9)
	{
		j=1;
		while(j<=i)
		{
			printf("%d*%d=%d\t",j,i,j*i);
			j++;
		}
		printf("\n");
		i++;
	}
	
	system("pause");
}