/* Note:Your choice is C IDE */
/* Author£ºGXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	char ch1;
	char ch2;
	char ch3;
	
	printf("ÇëÊäÈë×ÖÄ¸£º");
	scanf("%c",&ch1);
	scanf("%c",&ch2);
	scanf("%c",&ch3);
	
	if(ch1>ch2)
	{
		if(ch1>ch3)
		{
			if(ch2>ch3)
			{
				printf("%c %c %c",ch1,ch2,ch3);
			}
			else
			{
				printf("%c %c %c",ch1,ch3,ch2);
			}
		}
		else
		{
			printf("%c %c %c",ch3,ch1,ch2);
		}
	}
	else
	{
		if(ch2>ch3)
		{
			if(ch1>ch3)
			{
				printf("%c %c %c",ch2,ch1,ch3);
			}
			else
			{
				printf("%c %c %c",ch2,ch3,ch1);
			}
		}
		else
		{
			printf("%c %c %c",ch3,ch2,ch1);
		}
	}
	
	system("pause");
}