/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int number;
	int a;
	int b;
	int c;
	int sum;
	
	printf("请输入一个三位数：");
	scanf("%d",&number);
	
	if((number >=100) && (number <= 999))
	{
		a = number%10;
		b = (number/10)%10;
		c = number/100;
		sum = a+b+c;

		printf("这个三位数个位，十位，百位数字之和是：%d",sum);
	}
	else
	{
		printf("这不是个三位数！");
	}
	
	system("pause");
}

