/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void jitu();
void hou();
void fei();
void jian();

void main()
{
	int bianhao;
	while(1)
	{	
		printf("\t\t==========经典算法=============\n");
		printf("\t\t1.穷举法:鸡兔同笼问题\n");
		printf("\t\t2.递推法:猴子吃桃子\n");
		printf("\t\t3.迭代法:斐波那契数列非递归求法\n");
		printf("\t\t4.迭代法:剪绳子问题\n");
		printf("\t\t0.退出\n");
		printf("\t\t===============================\n");
		printf("请输入您的选择:");
		scanf("%d",&bianhao);
		switch(bianhao)
		{
			case 0:
				exit(0);
			case 1:
				jitu();
				break;
			case 2:
				hou();
				break;
			case 3:
				fei();
				break;
			case 4:
				jian();
				break;
			default:
				printf("选择有误!");
				break;
		}
	}
	system("pause");//防止exe文件闪退
}

void jitu()
{
	int i;
	printf("\n有若干只鸡兔在同一个笼子里,从上面数,有35个头;从下面数,有94只脚.求笼中各有几只鸡和兔?\n\n");
	for(i=1;i<=35;i++)
	{
		if(2*i+4*(35-i)==94)
		{
			printf("利用穷举法解题得结果:鸡%d只,兔子%d只\n",i,35-i);
		}
	}
}

void hou()
{
	int day;
	int num=1;
	printf("有数量未知的桃子,猴子第一天吃了总数量的一半又多吃一个,\n");
	printf("第二天又吃了剩下的一半又多吃一个,依次类推,到第十天桃子的数量仅剩一个,\n");
	printf("问最初桃子的数量有多少?\n");
	for(day=10;day>1;day--)
	{
		num=2*(num+1);
	}
	printf("桃子的数量是:%d个\n\n",num);
}

void fei()
{
	int i;
	int x=1;
	int y=1;
	int z;
	printf("有一对兔子不吃不喝不会死,第三个月成熟,从成熟开始每月繁殖生下一对兔子,\n");
	printf("新生的每对兔子仍是第三个月成熟开始每月生一对兔子,那么每个月兔子的对数如何计算.\n");
	printf("其实这就是著名数列斐波那契数列如下：1 1 2 3 5 8 13 21 34 ......\n");
	printf("打印前20项的值:\n");
	for(i=1;i<=20;i++)
	{
		if(i==1 || i==2)
		{
			printf("1\t");
		}
		else
		{
			z=x+y;
			printf("%d\t",z);
			x=y;
			y=z;
		}
		if(i%5==0)
		{
			printf("\n");
		}
	}printf("\n");
}

void jian()
{
	int i = 320;
	int day = 0;
	printf("一根绳子有320米长,每天截取12米,问多少天后绳子长度不足40米?\n");
	while(i>40)
	{
		day++;
		i-=12;
		printf("%d\t",i);
		if(day%6==0)
		{
			printf("\n");
		}
	}
	printf("\n总计需要%d天后绳子的长度不足40米\n",day);
}