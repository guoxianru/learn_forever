/* Note:Your choice is C IDE */
/* Author��GXR */
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
	printf("������˳���ĳ���:");
	scanf("%d",&chang);
	for(i=0;i<chang;i++)
	{
		printf("�������%d��Ԫ��:",i+1);
		scanf("%d",&s.a[i]);
		num++;
	}
	printf("������Ҫ�����Ԫ��:");
	scanf("%d",&ys);
	printf("������Ҫ������±�:");
	scanf("%d",&xb);
	if(xb<0 || xb>num-1)
	{
		printf("�����±�����!");
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
	
	system("pause");//��ֹexe�ļ�����
}