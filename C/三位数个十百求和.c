/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int number;
	int a;
	int b;
	int c;
	int sum;
	
	printf("������һ����λ����");
	scanf("%d",&number);
	
	if((number >=100) && (number <= 999))
	{
		a = number%10;
		b = (number/10)%10;
		c = number/100;
		sum = a+b+c;

		printf("�����λ����λ��ʮλ����λ����֮���ǣ�%d",sum);
	}
	else
	{
		printf("�ⲻ�Ǹ���λ����");
	}
	
	system("pause");
}

