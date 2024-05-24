#include <stdio.h>

int main(void)
{
	int x = 1;
	for (int i = 1; i < 10; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			int j1 = j % 10;
			if (j + j1 == i)
			{
				x = 0;
				break;
			}
		}
		if (x == 0)
		{
			x = 1;
			continue;
		}
		else
		{
			printf("%d\n", i);
			x = 1;
		}

	}

	x = 1;
	for (int i = 10; i < 100; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			int j1 = j / 100;
			int j2 = (j % 100) / 10;
			int j3 = (j % 100) % 10;
			if (j + j1 + j2 + j3 == i)
			{
				x = 0;
				break;
			}
		}
		if (x == 0)
		{
			x = 1;
			continue;
		}
		else
		{
			printf("%d\n", i);
			x = 1;
		}

	}

	x = 1;
	for (int i = 100; i < 1000; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			int j1 = j / 100;
			int j2 = (j % 100) / 10;
			int j3 = (j % 100) % 10;
			if (j + j1 + j2 + j3 == i)
			{
				x = 0;
				break;
			}
		}
		if (x == 0)
		{
			x = 1;
			continue;
		}
		else
		{
			printf("%d\n", i);
			x = 1;
		}

	}
	x = 1;
	for(int i = 1000; i <= 10000; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			int j1 = j / 1000;
			int j2 = (j % 1000) / 100;
			int j3 = ((j % 1000) % 100) / 10;
			int j4 = ((j % 1000) % 100) % 10;
			if (j + j1 + j2 + j3 + j4 == i)
			{
				x = 0;
				break;
			}
		}
		if (x == 0)
		{
			x = 1;
			continue;
		}
		else
		{
			printf("%d\n", i);
			x = 1;
		}

	}

}