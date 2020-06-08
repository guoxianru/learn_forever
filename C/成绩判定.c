/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int number;
	
	printf("请输入成绩:");
	scanf("%d",&number);
	
	if((number<0) || (number>100))
	{
		printf("输入成绩不合法!");
	}
	else if((number >= 0) && (number < 60))
	{
		printf("E");
	}
	else if((number >= 60) && (number < 70))
	{
		printf("D");
	}
	else if((number >= 70) && (number < 80))
	{
		printf("C");
	}
	else if((number >= 80) && (number < 90))
	{
		printf("B");
	}
	else if((number >= 90) && (number <= 100))
	{
		printf("A");
	}
	
	system("pause");
}