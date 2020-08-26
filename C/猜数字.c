/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int number = 24;
	int guessnum;
	int i;
	char en;
	

	
	printf("请输入一个数字：");
	scanf("%d",&guessnum);
	
	for(i = 1;i < 3;i++)
	{
		if(guessnum == number)
		{
			printf("恭喜你猜对了！");
			break;
		}
		else if(guessnum < number)
		{
			printf("猜大点！");
		}
		else if(guessnum > number)
		{
			printf("猜小点！");
		}
	}	 
	if(i == 3)
	{
		printf("继续请按ENTER，结束请按N");
		scanf("%c",&en);
		if(en != 'n')
		{
			i= 0;
		}
		else
		{
			printf("再见！");
		}
	}
	
	system("pause");
}