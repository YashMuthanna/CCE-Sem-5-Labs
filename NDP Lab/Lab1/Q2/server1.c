//BOILER PLATE UDP SERVER CONNECTIONLESS COMMUNICATION
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<stdio.h>

int main(){
	printf("Input port number: ");
	int x;
	scanf("%d", &x);
	struct sockaddr_in client, server;
	int sntb, recb;
	socklen_t len;
	int s = socket(AF_INET, SOCK_DGRAM, 0);
	if(s == -1){
		printf("SOCKET CREATION FAILED\n");
		close(s);
		exit(0);
	}
	printf("SOcket created....\n");
	server.sin_family = AF_INET;
	server.sin_port = htons(x);
	server.sin_addr.s_addr = htonl(INADDR_ANY);

	int ca;
	ca = sizeof(client);
	len = sizeof(client);
	char buff[100];
	int r = bind(s,(struct sockaddr*)&server,sizeof(server));
	if(r == -1){
		printf("BINDING FAILED\n");
		close(s);
		exit(0);
	}
	printf("Binding done successfully.. \n");
	while(1){
		recb = recvfrom(s,buff,sizeof(buff),0,(struct sockaddr*)&client, &ca);
		if (recb == -1) {
            printf("\nMessage Recieving Failed");
            close(s);
            exit(0);
        }
		if (!strcmp(buff, "halt"))
            break;
		printf("\nMessage Recieved: ");
        printf("%s\n", buff);
		char buff2[100];
		strcpy(buff2, buff);
		int n = strlen(buff2);
		int count=0;
		for(int i=0;i<n;i++){
			if(buff2[i] == 'a' || buff2[i] == 'e' || buff2[i] == 'o' || buff2[i] == 'i' || buff2[i] == 'u'){
				count++;
			}
		}
		buff[0] = n;
		buff[1] = count;
		buff[2] = 1;
		for(int i=0;i<n/2;i++){
			if( buff2[i] != buff2[n-i-1]){
				buff[2] = 0;
				break;
			}
		}
		sntb = sendto(s,buff,sizeof(buff),0,(struct sockaddr*)&client, len);
		if(sntb == -1){
			printf("Message sending failed..\n");
		}
	}
	close(s);
}
