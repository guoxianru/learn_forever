/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int num[6];
	int i;

	for (int i = 0; i <6; ++i)
	{
		printf("��������:");
		scanf("%d",&num[i]);
	}
	for (int i = 0; i <6; ++i)
	{
		printf("%d ",num[i]);
	}

	system("pause");//��ֹexe�ļ�����
}