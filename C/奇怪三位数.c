/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i;
	int x;
	int y;
	int z;
	
	for(i=100;i<=999;i++)
	{
		x=i%10;
		y=(i/10)%10;
		z=i/100;
		if(x+y+z==x*y*z)
		{
			if(x>z && z>y)
			{
				printf("��λ���ֱȰ�λ���ִ�,����λ�����ֱ�ʮλ���ִ�,���Ҹ�λ����֮�͵��ڸ�λ�������֮������λ����%d\n",i);
			}
		}
	}
	
	system("pause");
}