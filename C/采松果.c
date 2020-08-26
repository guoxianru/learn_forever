/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int day=112/14;
	
	for(i=1;i<=day;i++)
	{
		if(20*(day-i)+12*i==112)
		{
			printf("%d天下雨\n",i);
			break;
		}
	}
	
	system("pause");
}