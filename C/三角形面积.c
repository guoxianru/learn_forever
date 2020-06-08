/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int a;
	int b;
	int c;
	int s;
	int area;
	 
	printf("请输入三角形的一条边长：");
	scanf("%d" , &a);
	printf("请输入三角形的一条边长：");
	scanf("%d" , &b);
	printf("请输入三角形的一条边长：");
	scanf("%d" , &c);
	
	if((a+b>c) && (a+c>b) && (b+c>a))
	{
		s = 0.5*(a+b+c);
		area = sqrt(s*(s-a)*(s-b)*(s-c));
		printf("这个三角形的面积是%d" , area);
	}
	else
	{
		printf("这不是个三角形。");
	}
	
	system("pause");
}
