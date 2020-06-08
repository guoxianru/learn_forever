/* Note:Your choice is C IDE */
/* Author��GXR */
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
		printf("1.���\n");
		printf("2.����\n");
		printf("3.��ӡ��ͷ����β������Ʒ\n");
		printf("0.�˳�\n");
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
				printf("��������!\n");
		}
	}
	system("pause");//��ֹexe�ļ�����
}

void rudui()
{
	if((a.area+1)%MAXSIZE==a.front)
	{
		printf("���\n");	
	}
	else
	{
		printf("�����������Ʒ:\n");
		printf("\t��������Ʒ���:");
		scanf("%d",&a.s[a.area].bianhao);
		printf("\t��������Ʒ����:");
		scanf("%s",a.s[a.area].name);
		printf("\t��������Ʒ����:");
		scanf("%f",&a.s[a.area].price);
		printf("\t��������Ʒ����:");
		scanf("%s",a.s[a.area].label);
		a.area++;
		a.area=a.area%MAXSIZE;
		printf("��ӳɹ�\n");	
	}
}

void chudui()
{
	if(a.area==a.front)
	{
		printf("�ӿ�,û��Ԫ��\n");	
	}
	else
	{
		printf("���ӵ���Ʒ������%s,��Ʒ�����%d:\n",a.s[a.front].name,a.s[a.front].bianhao);
		a.front++;
		a.front=a.front%MAXSIZE;
	}
}

void dayin()
{
	for(i=a.front;i<a.area;i++)
	{
		printf("��Ʒ���:%d,��Ʒ����:%s,��Ʒ����:%.2f,��Ʒ����:%s\n",a.s[i].bianhao,a.s[i].name,a.s[i].price,a.s[i].label);
	}
}



