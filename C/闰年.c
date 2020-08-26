/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int a;
	
	printf("输入年份:");
	scanf("%d",&a);
	
	if(((a%4==0) && (a%100!=0)) || (a%400==0))
	{
		printf("闰年");
	}
	else
	{
		printf("非闰");
	}
	
	system("pause");
}