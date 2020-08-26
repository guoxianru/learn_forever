/* Note:Your choice is C IDE */
/* Author：GXR */
#include "stdio.h"
#include "windows.h"
#define MAXSIZE 5
void jin();
void chu();
void dayin();

struct student
{
	int xh;
	char name[10];
	char add[10];
	int tel;
};
struct stack
{
	struct student s[MAXSIZE];
	int top;
};
struct stack a;

void main()
{
	a.top=-1;
	int bianhao;
	while(1)
	{
		printf("++++++++++++++++++++\n");
		printf("1.进栈\n");
		printf("2.出栈\n");
		printf("3.打印从栈顶到栈底的所有元素\n");
		printf("0.退出\n");
		printf("++++++++++++++++++++\n");
		scanf("%d",&bianhao);
		switch(bianhao)
		{
			case 1:
				jin();
				break;
			case 2:
				chu();
				break;
			case 3:
				dayin();
				break;
			case 0:
				exit(0);
			default:
				printf("选择错误!\n");
				break;
		}
	}
	system("pause");//防止exe文件闪退
}

void jin()
{
	if(a.top==MAXSIZE-1)
	{
		printf("满栈!\n");
	}
	else
	{
		a.top++;
		printf("请输入要进栈的学生信息:\n");
		printf("请输入学生的学号:");
		scanf("%d",&a.s[a.top].xh);
		printf("请输入学生的姓名:");
		scanf("%s",a.s[a.top].name);
		printf("请输入学生的籍贯:");
		scanf("%s",a.s[a.top].add);
		printf("请输入学生的电话:");
		scanf("%d",&a.s[a.top].tel);
		printf("进栈成功!\n");
	}
}

void chu()
{
	if(a.top==-1)
	{
		printf("空栈!\n");
	}
	else
	{
		printf("出栈的学生是%s\n",a.s[a.top--].name);
	}
}

void dayin()
{
	int i;
	printf("从栈顶到栈底的所有元素是:\n");
	for(i=a.top;i>-1;i--)
	{
		printf("学号:%d,姓名:%s,籍贯:%s,手机号:%d\n",a.s[i].xh,a.s[i].name,a.s[i].add,a.s[i].tel);
	}
}








