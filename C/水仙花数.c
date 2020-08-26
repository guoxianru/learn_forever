/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
void main()
{
	int i=100;
	int a;
	int b;
	int c;
	
	while(i<1000)
	{
		a = i%10;
		b = (i/10)%10;
		c = i/100;
		if(i == a*a*a + b*b*b + c*c*c)
		{
			printf("%d\n",i);
		}
		i++;
	}
	
	system("pause");
}