/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int num;
	
	for(i=1;;i++)
	{
		if(10*i-2==12*(i-1))
		{
			printf("%d只船\n",i);
			break;
		}
	}
	
	system("pause");
}