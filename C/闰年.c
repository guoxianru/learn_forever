/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int a;
	
	printf("�������:");
	scanf("%d",&a);
	
	if(((a%4==0) && (a%100!=0)) || (a%400==0))
	{
		printf("����");
	}
	else
	{
		printf("����");
	}
	
	system("pause");
}