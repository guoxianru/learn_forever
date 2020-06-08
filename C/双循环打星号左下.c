/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int j;
	int m;
	
	printf("几行几列:");
	scanf("%d",&m);
	
	i=1;
	while(i<=m)
	{
		j=1;
		while(j<=i)
		{
			
			printf("*");
			j++;
		}
		printf("\n");
		i++;
	}
	
	system("pause");
}