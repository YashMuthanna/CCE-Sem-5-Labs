//BOILER PLATE UDP CLIENT
#include<stdio.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<sys/stat.h>
#include<netinet/in.h>
#include<fcntl.h>

int main(){
	int x;
	printf("Input port number: ");
	scanf("%d", &x);
	struct sockaddr_in client, server;
	char buff[50];
	int s = socket(AF_INET, SOCK_DGRAM, 0);
	socklen_t len;
	if(s == -1){
		printf("Connection failed\n");
		exit(0);
	}	
	printf("Socket created\n");
	server.sin_family = AF_INET;
	server.sin_port = htons(x);
	server.sin_addr.s_addr = inet_addr("127.0.0.1");
	int sa;
	sa = sizeof(server);
	len = sizeof(server);
	int sntb, recb;
	while(1){
		printf("\n\n");
		printf("Type message: ");
		scanf("%s", buff);
		sntb = sendto(s, buff, sizeof(buff), 0, (struct sockaddr*)&server, len);
		if(sntb == -1){
			printf("message send failed\n");
			exit(0);
		}
		if (!strcmp(buff, "halt"))
            break;
		recb = recvfrom(s, buff, sizeof(buff), 0, (struct sockaddr*)&server, &sa);
		if(recb==-1)
		{
			printf("\nMessage Recieving Failed");	
			close(s);
			exit(0);
		}
		if(buff[2] == 1){
			printf("It is a palindrome\n");
			printf("No. of vowels: %d\n", buff[1]);
			printf("Length: %d\n", buff[0]);
		}
		else{
			printf("It is NOT a palindrome\n");
			printf("No. of vowels: %d\n", buff[1]);
			printf("Length: %d\n", buff[0]);
		}
		
	}
	close(s);
}
