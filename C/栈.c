/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
#define MAXSIZE 5
void jin();
void chu();
void dayin();

struct student
{
	int xh;
	char name[10];
	char add[10];
	int tel;
};
struct stack
{
	struct student s[MAXSIZE];
	int top;
};
struct stack a;

void main()
{
	a.top=-1;
	int bianhao;
	while(1)
	{
		printf("++++++++++++++++++++\n");
		printf("1.��ջ\n");
		printf("2.��ջ\n");
		printf("3.��ӡ��ջ����ջ�׵�����Ԫ��\n");
		printf("0.�˳�\n");
		printf("++++++++++++++++++++\n");
		scanf("%d",&bianhao);
		switch(bianhao)
		{
			case 1:
				jin();
				break;
			case 2:
				chu();
				break;
			case 3:
				dayin();
				break;
			case 0:
				exit(0);
			default:
				printf("ѡ�����!\n");
				break;
		}
	}
	system("pause");//��ֹexe�ļ�����
}

void jin()
{
	if(a.top==MAXSIZE-1)
	{
		printf("��ջ!\n");
	}
	else
	{
		a.top++;
		printf("������Ҫ��ջ��ѧ����Ϣ:\n");
		printf("������ѧ����ѧ��:");
		scanf("%d",&a.s[a.top].xh);
		printf("������ѧ��������:");
		scanf("%s",a.s[a.top].name);
		printf("������ѧ���ļ���:");
		scanf("%s",a.s[a.top].add);
		printf("������ѧ���ĵ绰:");
		scanf("%d",&a.s[a.top].tel);
		printf("��ջ�ɹ�!\n");
	}
}

void chu()
{
	if(a.top==-1)
	{
		printf("��ջ!\n");
	}
	else
	{
		printf("��ջ��ѧ����%s\n",a.s[a.top--].name);
	}
}

void dayin()
{
	int i;
	printf("��ջ����ջ�׵�����Ԫ����:\n");
	for(i=a.top;i>-1;i--)
	{
		printf("ѧ��:%d,����:%s,����:%s,�ֻ���:%d\n",a.s[i].xh,a.s[i].name,a.s[i].add,a.s[i].tel);
	}
}








