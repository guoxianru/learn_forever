/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int n1;
	int n2;
	int n3;
	int _max;
	int _min;
	
	printf("输入三个数字:");
	scanf("%d%d%d",&n1,&n2,&n3);
	
	_max = n1;
	if(n2>_max)
	{
		_max = n2;
	}
	if(n3>_max)
	{
		_max = n3;
	}
	_min = n1;
	if(n2<_min)
	{
		_min = n2;
	}
	if(n3<_min)
	{
		_min = n3;
	}
	printf("这三个数字中最大值%d和最小值%d的平方差是%d",_max,_min,_max*_max-_min*_min);
	
	system("pause");
}	