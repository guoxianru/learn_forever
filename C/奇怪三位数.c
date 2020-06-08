/* Note:Your choice is C IDE */
/* Author：GXR */
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
				printf("个位数字比百位数字大,而百位数字又比十位数字大,并且各位数字之和等于各位数字相乘之积的三位数是%d\n",i);
			}
		}
	}
	
	system("pause");
}