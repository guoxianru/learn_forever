/* Note:Your choice is C IDE */
/* Author��GXR */
#include "stdio.h"
#include "windows.h"

void main()
{
	int x;
	int y;
	int z;

	for(x=1;x<=100;x++)
	{
		for(y=1;y<=100;y++)
		{
			z=100-x-y;
			if(x*5+y*3+z/3==100)
			{
				if(z%3==0)
				{
					printf("����:%d\nĸ��:%d\nС��:%d\n\n",x,y,z);
				}
			}
		}
	}
	system("pause");//��ֹexe�ļ�����
} 