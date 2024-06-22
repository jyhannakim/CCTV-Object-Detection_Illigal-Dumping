#pragma warning(disable : 4996)
#include <conio.h>
#include <stdio.h>
int main(void) {
	double x, y, result;
	printf("두 개의 실수를 입력하시오 :");
	scanf("%lf %lf", &x, &y);
	result = x+y;
	printf("%.2f + %.2f = %.2f \n", x, y, result);
	result = x-y;
	printf("%.2f - %.2f = %.2f \n", x, y, result);
	result = x*y;
	printf("%.2f * %.2f = %.2f \n", x, y, result);
	result = x/y;
	printf("%.2f / %.2f = %.2f \n", x, y, result);
	getch();
	return 0;
	/*int x;
	int y;
	printf("두 개의 정수를 입력하시오 :");
	scanf("%d %d", &x, &y);
	printf("%d + %d = %d \n", x, y, x + y);
	printf("%d - %d = %d \n", x, y, x - y);
	printf("%d * %d = %d \n", x, y, x * y);
	printf("%d / %d = %.2f \n", x, y, (float)x / y);
	printf("%d %% %d = %d \n", x, y, x % y);
	getch();
	return 0;
	*/
	/*int x;
	int y;
	
	printf("두 개의 정수를 입력하시오 :");
	scanf("%d %d", &x, &y);
	printf("%d + %d = %d \n", x, y, x + y);
	printf("%d - %d = %d \n", x, y, x - y);
	printf("%d * %d = %d \n", x, y, x * y);
	printf("%d / %d = %.2f \n", x, y, (float)x / y);
	printf("%d %% %d = %d \n", x, y, x % y);
	getch();
	return 0;
	*/
	/*int x;
	int y;

	printf("두 개의 정수를 입력하시오 :");
	scanf("%d %d", &x, &y);
	printf("%d + %d = %d \n", x, y, x + y);
	printf("%d - %d = %d \n", x, y, x - y);
	printf("%d * %d = %d \n", x, y, x * y);
	printf("%d / %d = %.2f \n", x, y, (float)x /(float)y);
	printf("%d / %d = %.2f \n", x, y, x /(float)y);
	printf("%d / %d = %.2f \n", x, y, (float)x /y);
	printf("%d %% %d = %d \n", x, y, x % y);
	getch();
	return 0;
	*/
	/*

	int x = 1;
	int y = 2;
	int z = 3;
	printf("%d\n", x ? y : z);
	getch();
	return 0;
	*/

}