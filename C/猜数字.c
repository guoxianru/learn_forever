/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int number = 24;
	int guessnum;
	int i;
	char en;
	

	
	printf("������һ�����֣�");
	scanf("%d",&guessnum);
	
	for(i = 1;i < 3;i++)
	{
		if(guessnum == number)
		{
			printf("��ϲ��¶��ˣ�");
			break;
		}
		else if(guessnum < number)
		{
			printf("�´�㣡");
		}
		else if(guessnum > number)
		{
			printf("��С�㣡");
		}
	}	 
	if(i == 3)
	{
		printf("�����밴ENTER�������밴N");
		scanf("%c",&en);
		if(en != 'n')
		{
			i= 0;
		}
		else
		{
			printf("�ټ���");
		}
	}
	
	system("pause");
}