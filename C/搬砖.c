/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int x;
	int y;
	int z;

	for(x=1;x<=36/4;x++)
	{
		for(y=1;y<=36/3;y++)
		{
			z=36-x-y;
			if(x*4+y*3+z/2==36)
			{
				if(z%2==0)
				{
					printf("男:%d\n女:%d\n小孩:%d\n",x,y,z);
				}
			}
		}
	}
	
	system("pause");
} 