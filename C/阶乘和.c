/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int j=1;
	int n;
	int sum;
	
	printf("输入一个数:");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		j*=i;
		sum+=j;
	}
	printf("%d阶乘和是%d\n",n,sum);
	
	system("pause");
}