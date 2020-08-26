/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int j;
	int flag;
	int n;
	
	i=2;
	while(i<=100)
	{
		j=2;
		flag=0;
		while(j<i)
		{
			if(i%j==0)
			{
				flag=1;
			}
			j++;
		}
		if(flag==0)
		{
			printf("%d ",i);
		}
		i++;
	}
	
	system("pause");
}