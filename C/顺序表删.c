/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
#define MAXSIZE 100
struct slist
{
	int a[MAXSIZE];
	int len;
};

void main()
{
	struct slist s={{0,1,2,3,4,5,6,7,8,9},10};
	int i;
	int xb;
	
	printf("请输入要删除元素的下标:");
	scanf("%d",&xb);
	if(xb<0 || xb>9)
	{
		printf("Error!\n");
	}
	else
	{
		for(i=xb;i<9;i++)
		{
			s.a[i]=s.a[i+1];
		}
		for(i=0;i<9;i++)
		{
			printf("%d\t",s.a[i]);
		}
	}
	printf("\n");
	
	system("pause");//防止exe文件闪退
}