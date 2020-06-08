/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void youping();//函数声明
void pajing();
void tuzi();
void gonglu();

void main()
{
	int bianhao;
	while(1)//循环显示主界面
	{
		printf("\n\t\t=========经典算法==============\n");
		printf("\t\t1.穷举法:大小油瓶问题\n");
		printf("\t\t2.迭代法:蜗牛爬井问题\n");
		printf("\t\t3.迭代法:斐波那契数列非递归求法\n");
		printf("\t\t4.迭代法:修公路问题\n");
		printf("\t\t0.退出\n");
		printf("\t\t===============================\n");
		printf("请输入您的选择:");
		scanf("%d",&bianhao);
		switch(bianhao)//选择编号
		{
			case 0:
				exit(0);//退出整个程序
			case 1:
				youping();//调用子函数
				break;
			case 2:
				pajing();//调用子函数
				break;
			case 3:
				tuzi();//调用子函数
				break;
			case 4:
				gonglu();//调用子函数
				break;
			default:
				printf("选择有误!");//选择有误提示
				break;
		}
	}
	system("pause");//防止exe文件闪退
}

void youping()
{
	int da;
	printf("\n大油瓶每瓶装4千克,小油瓶2瓶装1千克,现有100千克油装了60个瓶子.问大小油瓶各多少个?\n");
	for(da=1;da<=60;da++)
	{
		if(da*4+(60-da)/2==100)
		{
			printf("\n利用穷举法解题得结果:大油瓶%d个,小油瓶%d个.",da,60-da);
		}
	}
}

void pajing()
{
	int day;
	int sum=20;
	printf("一口枯井有20米深,蜗牛从井底开始白天爬5米,晚上滑落3米,问多少天后可爬到井上?\n");
	for(day=0;;day++)
	{
		sum-=5;
		sum+=3;
		if(sum==0)
			{
				printf("蜗牛爬出来需要%d天",day);
				break;
			}
	}
}

void tuzi()
{
	int num;
	int i;
	int x=1;
	int y=1;
	int z;
	printf("有一对兔子不吃不喝不会死,第三个月成熟,从成熟开始每月繁殖生下一堆兔子,\n");
	printf("新生的每对兔子仍是第三个月成熟开始每月生一对兔子,那么每个月兔子的对数如何计算.\n");
	printf("其实这就是著名数列斐波那契数列如下:1 1 2 3 5 8 13 21 34 ......\n");
	printf("请输入打印的项数(大于2):\n");
	scanf("%d",&num);
	for(i=1;i<=num;i++)
	{
		if(i==1 || i==2)
		{
			printf("1\t");
		}
		else
		{
			z=x+y;
			printf("%d\t",z);
			y=x;
			x=z;
		}
		if(i%5==0)
		{
			printf("\n");
		}
	}
}

void gonglu()
{
	int day=0;
	int sum=1000;
	printf("一条待修公路1000公里,每天修55公里,问多少天后还有不足60公里未修?\n");
	while(sum>60)
	{
		printf("%d\t",sum);
		day++;
		sum-=55;
		if(day%6==0)
		{
			printf("\n");
		}
	}
	printf("\n总计需要%d天后还有不足60公里未修",day);
}