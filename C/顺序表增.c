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
	struct slist s;
	int i;
	int chang;
	int num=0;
	int ys;
	int xb;
	printf("请输入顺序表的长度:");
	scanf("%d",&chang);
	for(i=0;i<chang;i++)
	{
		printf("请输入第%d个元素:",i+1);
		scanf("%d",&s.a[i]);
		num++;
	}
	printf("请输入要插入的元素:");
	scanf("%d",&ys);
	printf("请输入要插入的下标:");
	scanf("%d",&xb);
	if(xb<0 || xb>num-1)
	{
		printf("输入下标有误!");
	}
	else
	{
		for(i=num-1;i>=xb;i--)
		{
			s.a[i+1]=s.a[i];
		}
		s.a[xb]=ys;
		num++;
		for(i = 0;i<num;i++)
		{
			printf("%d\t",s.a[i]);
		}
	}
	printf("\n");
	
	system("pause");//防止exe文件闪退
}