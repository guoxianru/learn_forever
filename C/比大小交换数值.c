/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int a;
	int b;
	int c;
	
	printf("请输入两个数字:");
	scanf("%d %d",&a,&b);
	
	if(a>b)
	{
		printf("a%d>b%d",a,b);
	}
	else
	{
		c = a;
		a = b;
		b = c;
		printf("a%d>b%d",a,b);
	}
	
	system("pause");
}