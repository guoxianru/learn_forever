/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int a;
	int b;
	int c;
	int s;
	int area;
	 
	printf("�����������ε�һ���߳���");
	scanf("%d" , &a);
	printf("�����������ε�һ���߳���");
	scanf("%d" , &b);
	printf("�����������ε�һ���߳���");
	scanf("%d" , &c);
	
	if((a+b>c) && (a+c>b) && (b+c>a))
	{
		s = 0.5*(a+b+c);
		area = sqrt(s*(s-a)*(s-b)*(s-c));
		printf("��������ε������%d" , area);
	}
	else
	{
		printf("�ⲻ�Ǹ������Ρ�");
	}
	
	system("pause");
}
