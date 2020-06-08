/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int j;
	int m;
	int n;
	
	printf("几行几列:");
	scanf("%d%d",&m,&n);
	i=1;
	while(i<=m)
	{
		j=1;
		while(j<=n)
		{
			
			printf("*");
			j++;
		}
		printf("\n");
		i++;
	}
	
	system("pause");
}