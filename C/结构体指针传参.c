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
	struct student a = {"����",22};
	fun(&a);
	
	system("pause");//��ֹexe�ļ�����
}

void fun(struct student *b)
{
	printf("%s %d \n",b->name,b->age);
}
	
