/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int a;
	int b;
	int c;
	int d;
	int e;
	int _max;
	int _min;
	
	printf("输入五个数字:");
	scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
	
	_max = a;
	if(b>_max)
	{
		_max = b;
	}
	if(c>_max)
	{
		_max = c;
	}
	if(d>_max)
	{
		_max = d;
	}
	if(e>_max)
	{
		_max = e;
	}
	
	_min = a;
	if(b<_min)
	{
		_min = b;
	}
	if(c<_min)
	{
		_min = c;
	}
	if(d<_min)
	{
		_min = d;
	}
	if(e<_min)
	{
		_min = e;
	}
	printf("这五个数字中最大值是%d,最小值是%d\n",_max,_min);
	
	system("pause");
}	