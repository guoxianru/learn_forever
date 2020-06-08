/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"

void main()
{
	int a=1,b=1,c,i;
    printf("打印前20项的值:\n");
    printf("%d\n%d\n",a,b);
    for(i=3;i<=20;i++)
	{
		c=a+b;
        printf("%d\n",c);
        a=b;    
        b=c;
	}
	system("pause");//防止exe文件闪退
}
