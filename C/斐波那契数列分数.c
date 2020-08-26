/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i=1;
	float fz=2;
	float fm=1;
	float sum=0;
	
	while(i<=20)
	{
		sum+=(fz/fm);
        fz=fz+fm;
		fm=fz-fm;
		i++;
	}
	
	printf("前20项和是%.2f\n",sum);
	
	system("pause");
}
