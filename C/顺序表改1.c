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
	int ys;
	int flag=0;
	
	printf("请输入要修改的下标:");
	scanf("%d",&xb);
	printf("请输入要修改的元素:");
	scanf("%d",&ys);
	if(xb<0 || xb>9)
	{
		printf("没有该下标!\n");
	}
	else
	{
		s.a[xb]=ys;
		for(i=0;i<10;i++)
		{
			printf("%d\t",s.a[i]);
		}
		printf("\n");
	}
	
	system("pause");//防止exe文件闪退
}