/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void youping();//��������
void pajing();
void tuzi();
void gonglu();

void main()
{
	int bianhao;
	while(1)//ѭ����ʾ������
	{
		printf("\n\t\t=========�����㷨==============\n");
		printf("\t\t1.��ٷ�:��С��ƿ����\n");
		printf("\t\t2.������:��ţ��������\n");
		printf("\t\t3.������:쳲��������зǵݹ���\n");
		printf("\t\t4.������:�޹�·����\n");
		printf("\t\t0.�˳�\n");
		printf("\t\t===============================\n");
		printf("����������ѡ��:");
		scanf("%d",&bianhao);
		switch(bianhao)//ѡ����
		{
			case 0:
				exit(0);//�˳���������
			case 1:
				youping();//�����Ӻ���
				break;
			case 2:
				pajing();//�����Ӻ���
				break;
			case 3:
				tuzi();//�����Ӻ���
				break;
			case 4:
				gonglu();//�����Ӻ���
				break;
			default:
				printf("ѡ������!");//ѡ��������ʾ
				break;
		}
	}
	system("pause");//��ֹexe�ļ�����
}

void youping()
{
	int da;
	printf("\n����ƿÿƿװ4ǧ��,С��ƿ2ƿװ1ǧ��,����100ǧ����װ��60��ƿ��.�ʴ�С��ƿ�����ٸ�?\n");
	for(da=1;da<=60;da++)
	{
		if(da*4+(60-da)/2==100)
		{
			printf("\n������ٷ�����ý��:����ƿ%d��,С��ƿ%d��.",da,60-da);
		}
	}
}

void pajing()
{
	int day;
	int sum=20;
	printf("һ�ڿݾ���20����,��ţ�Ӿ��׿�ʼ������5��,���ϻ���3��,�ʶ���������������?\n");
	for(day=0;;day++)
	{
		sum-=5;
		sum+=3;
		if(sum==0)
			{
				printf("��ţ��������Ҫ%d��",day);
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
	printf("��һ�����Ӳ��Բ��Ȳ�����,�������³���,�ӳ��쿪ʼÿ�·�ֳ����һ������,\n");
	printf("������ÿ���������ǵ������³��쿪ʼÿ����һ������,��ôÿ�������ӵĶ�����μ���.\n");
	printf("��ʵ�������������쳲�������������:1 1 2 3 5 8 13 21 34 ......\n");
	printf("�������ӡ������(����2):\n");
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
	printf("һ�����޹�·1000����,ÿ����55����,�ʶ�������в���60����δ��?\n");
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
	printf("\n�ܼ���Ҫ%d����в���60����δ��",day);
}