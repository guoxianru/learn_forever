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
	struct slist s={{0,1,2,3,4,5,6,7,8,9},10};
	int i;
	int ys;
	int flag=0;
	
	printf("������Ҫ���ҵ�Ԫ��:");
	scanf("%d",&ys);
	for(i=0;i<10;i++)
	{
		if(ys==s.a[i])
		{
			printf("��Ԫ���ڵ�%d��λ��!\n",i+1);
			flag=1;
		}
	}
	if(flag==0)
	{
		printf("û�и�Ԫ��!\n");
	}
	
	system("pause");//��ֹexe�ļ�����
}