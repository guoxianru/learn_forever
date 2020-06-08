/* Note:Your choice is C IDE */
/* Author：GXR */
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
		printf("请输入要计算的数字：");
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
					printf("除数不能为0");
					break;
				}
			default:
				printf("输入不正确");
				break;
		}
		printf("继续输入y,退出输入n!");
		getchar();
		scanf("%c",&jx);
		getchar();
	}
	
	system("pause");
}