/* Note:Your choice is C IDE */
/* Author:GXR */
#include "stdio.h"
#include "windows.h"
void fun();
struct student
{
	char name[20];
	int age;
};

void main()
{
	struct student a = {"王五",22};
	fun(&a);
	
	system("pause");//防止exe文件闪退
}

void fun(struct student *b)
{
	printf("%s %d \n",b->name,b->age);
}
	
