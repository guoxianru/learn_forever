/* Note:Your choice is C IDE */
/* Author��GXR */
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
		printf("\t\t==========�����㷨=============\n");
		printf("\t\t1.��ٷ�:����ͬ������\n");
		printf("\t\t2.���Ʒ�:���ӳ�����\n");
		printf("\t\t3.������:쳲��������зǵݹ���\n");
		printf("\t\t4.������:����������\n");
		printf("\t\t0.�˳�\n");
		printf("\t\t===============================\n");
		printf("����������ѡ��:");
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
				printf("ѡ������!");
				break;
		}
	}
	system("pause");//��ֹexe�ļ�����
}

void jitu()
{
	int i;
	printf("\n������ֻ������ͬһ��������,��������,��35��ͷ;��������,��94ֻ��.�����и��м�ֻ������?\n\n");
	for(i=1;i<=35;i++)
	{
		if(2*i+4*(35-i)==94)
		{
			printf("������ٷ�����ý��:��%dֻ,����%dֻ\n",i,35-i);
		}
	}
}

void hou()
{
	int day;
	int num=1;
	printf("������δ֪������,���ӵ�һ�������������һ���ֶ��һ��,\n");
	printf("�ڶ����ֳ���ʣ�µ�һ���ֶ��һ��,��������,����ʮ�����ӵ�������ʣһ��,\n");
	printf("��������ӵ������ж���?\n");
	for(day=10;day>1;day--)
	{
		num=2*(num+1);
	}
	printf("���ӵ�������:%d��\n\n",num);
}

void fei()
{
	int i;
	int x=1;
	int y=1;
	int z;
	printf("��һ�����Ӳ��Բ��Ȳ�����,�������³���,�ӳ��쿪ʼÿ�·�ֳ����һ������,\n");
	printf("������ÿ���������ǵ������³��쿪ʼÿ����һ������,��ôÿ�������ӵĶ�����μ���.\n");
	printf("��ʵ�������������쳲������������£�1 1 2 3 5 8 13 21 34 ......\n");
	printf("��ӡǰ20���ֵ:\n");
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
	printf("һ��������320�׳�,ÿ���ȡ12��,�ʶ���������ӳ��Ȳ���40��?\n");
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
	printf("\n�ܼ���Ҫ%d������ӵĳ��Ȳ���40��\n",day);
}