/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	char ch;
	float num1;
	float num2;
	float sum;
	char jx='y';
	
	while(jx == 'y')
	{
		printf("������Ҫ��������֣�");
		scanf("%f%c%f",&num1,&ch,&num2);
	
		switch(ch)
		{
			case '+':
				sum = num1 + num2;
				printf("%.2f+%.2f=%.2f\n",num1,num2,sum);
				
				break;
			case '-':
				sum = num1 - num2;
				printf("%.2f-%.2f=%.2f\n",num1,num2,sum);
				break;
			case '*':
				sum = num1 * num2;
				printf("%.2f*%.2f=%.2f\n",num1,num2,sum);
				break;
			case '/':
				sum = num1 / num2;
				if(num2 != 0)
				{
					printf("%.2f/%.2f=%.2f\n",num1,num2,sum);
					break;
				}
				else
				{
					printf("��������Ϊ0");
					break;
				}
			default:
				printf("���벻��ȷ");
				break;
		}
		printf("��������y,�˳�����n!");
		getchar();
		scanf("%c",&jx);
		getchar();
	}
	
	system("pause");
}