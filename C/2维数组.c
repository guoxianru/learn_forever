/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int n[3][2];
	int i;
	int j;

	for(i=0;i<3;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("输入数字:");
			scanf("%d",&n[i][j]);
		}
	}

	for(i=0;i<3;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("%d ",n[i][j]);
		}
		printf("\n");
	}

	system("pause");//防止exe文件闪退
}