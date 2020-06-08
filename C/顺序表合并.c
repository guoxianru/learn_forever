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
	struct slist la={{1,3,5,7,9},5}; //定义顺序表la,lb并赋初值。
	struct slist lb={{2,4,6,8},4};
	struct slist lc;  //合并后的顺序表lc
	int i;
	int x=0;//x标识la顺序表的下标
	int y=0;//y标识lb顺序表的下标
	int z=0;//z标识lc顺序表的下标
	
	while(x<la.len && y<lb.len)   //当一个表的元素放完退出循环
	{
		if(la.a[x]<=lb.a[y])     //将小的放到新顺序表中
		{
			lc.a[z]=la.a[x];
			x++;
			z++;
		}
		else 
		{
			lc.a[z]=lb.a[y];
			y++;
			z++;
		}
	}
	
	while(x<la.len)   //la表未结束还有元素,将剩余元素加到lc表
	{
			lc.a[z]=la.a[x];
			x++;
			z++;
	}
	
	while(y<lb.len)  //lb表未结束还有元素,将剩余元素加到lc表
	{
			lc.a[z]=lb.a[y];
			y++;
			z++;
	}
	
	for(i=0;i<z;i++)  //输出合并后的顺序表
	{
		printf("%d\t",lc.a[i]);
	}
	printf("\n");
}
