/* Note:Your choice is C IDE */
/* Author£ºGXR */
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
			printf("%dÌìÏÂÓê\n",i);
			break;
		}
	}
	
	system("pause");
}