/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int j=1;
	int n;
	int sum;
	
	printf("����һ����:");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		j*=i;
		sum+=j;
	}
	printf("%d�׳˺���%d\n",n,sum);
	
	system("pause");
}