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
	struct slist la={{1,3,5,7,9},5}; //����˳���la,lb������ֵ��
	struct slist lb={{2,4,6,8},4};
	struct slist lc;  //�ϲ����˳���lc
	int i;
	int x=0;//x��ʶla˳�����±�
	int y=0;//y��ʶlb˳�����±�
	int z=0;//z��ʶlc˳�����±�
	
	while(x<la.len && y<lb.len)   //��һ�����Ԫ�ط����˳�ѭ��
	{
		if(la.a[x]<=lb.a[y])     //��С�ķŵ���˳�����
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
	
	while(x<la.len)   //la��δ��������Ԫ��,��ʣ��Ԫ�ؼӵ�lc��
	{
			lc.a[z]=la.a[x];
			x++;
			z++;
	}
	
	while(y<lb.len)  //lb��δ��������Ԫ��,��ʣ��Ԫ�ؼӵ�lc��
	{
			lc.a[z]=lb.a[y];
			y++;
			z++;
	}
	
	for(i=0;i<z;i++)  //����ϲ����˳���
	{
		printf("%d\t",lc.a[i]);
	}
	printf("\n");
}
