/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int s[10];
	int i;
	int j;
	int temp;
	for(i=0;i<10;i++)
	{
		printf("输入第%d个整数:",i+1);
		scanf("%d",&s[i]);
	}
	for(i=0;i<9;i++)
	{
		for(j=0;j<9-i;j++)
		{
			if(s[j]>s[j+1])
			{
				temp=s[j];
				s[j]=s[j+1];
				s[j+1]=temp;
			}
		}
	}
	for(i=0;i<10;i++)
	{
		printf("%d ",s[i]);
	}
	
	system("pause");//防止exe文件闪退
}