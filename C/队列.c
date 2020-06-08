/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
#define MAXSIZE 5
void rudui();
void chudui();
void dayin();

struct shangpin
{
	int bianhao;
	char name[20];
	float price;
	char label[20];
};
struct queue
{
	struct shangpin s[MAXSIZE];
	int area;
	int front;
};
struct queue a;
int bh;
int i;

void main()
{
	a.area=0;
	a.front=0;
	while(1)
	{
		printf("==========================\n");
		printf("1.入队\n");
		printf("2.出队\n");
		printf("3.打印队头到队尾所有商品\n");
		printf("0.退出\n");
		printf("==========================\n");
		scanf("%d",&bh);
		switch(bh)
		{
			case 1:
				rudui();
				break;
			case 2:
				chudui();
				break;
			case 3:
				dayin();
				break;
			case 0:
				exit(0);
			default:
				printf("输入有误!\n");
		}
	}
	system("pause");//防止exe文件闪退
}

void rudui()
{
	if((a.area+1)%MAXSIZE==a.front)
	{
		printf("溢出\n");	
	}
	else
	{
		printf("请输入入队商品:\n");
		printf("\t请输入商品编号:");
		scanf("%d",&a.s[a.area].bianhao);
		printf("\t请输入商品名称:");
		scanf("%s",a.s[a.area].name);
		printf("\t请输入商品单价:");
		scanf("%f",&a.s[a.area].price);
		printf("\t请输入商品描述:");
		scanf("%s",a.s[a.area].label);
		a.area++;
		a.area=a.area%MAXSIZE;
		printf("入队成功\n");	
	}
}

void chudui()
{
	if(a.area==a.front)
	{
		printf("队空,没有元素\n");	
	}
	else
	{
		printf("出队的商品名称是%s,商品编号是%d:\n",a.s[a.front].name,a.s[a.front].bianhao);
		a.front++;
		a.front=a.front%MAXSIZE;
	}
}

void dayin()
{
	for(i=a.front;i<a.area;i++)
	{
		printf("商品编号:%d,商品名称:%s,商品单价:%.2f,商品描述:%s\n",a.s[i].bianhao,a.s[i].name,a.s[i].price,a.s[i].label);
	}
}



