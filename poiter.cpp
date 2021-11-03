#include <stdio.h>
#include <cstring>
#define BUFFERSIZE 256
int main(int argc, char *argv[])
{
	char buffer[BUFFERSIZE];
	if (argc < 2)
		return -1;
	else
	{
		strcpy(buffer, argv[1]);
		return 0;
	}
}
