#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>

#define MAX 100

int main() {
    int recb, res;

    int PORT;
    printf("Input PORT: ");
    scanf("%d", &PORT);

    struct sockaddr_in server;
    int s = socket(AF_INET, SOCK_STREAM, 0);
    if(s == -1){
        printf("Error creating socket...\n");
        close(s);
        exit(0);
    }
    printf("socket created!!\n");
    server.sin_addr.s_addr = inet_addr("127.0.0.1"); 
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    printf("Ready to connect!");

    // Connecting
    connect(s, (struct sockaddr*)&server, sizeof(server)) < 0 ? perror("\nConnection error.") : printf("\nSocket connected.");

    int choice=0;
    char buff[50];
    char buff2[50];
    int arr[10];
    int n;
    printf("Enter number of elements in array: ");
    scanf("%d", &n);
    printf("Enter array elements: ");
    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    res = send(s, arr, sizeof(arr), 0);
    if(res == -1){
        printf("Failed to send array\n");
        close(s);
        exit(0);
    }
    printf("Array Sent successfully\n");
    while(choice!=5){
        printf("Enter your choice\n1.Search for a number\n2.Sort in ascending\n3.Sort descending\n4.Split\n5.EXIT\n");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                buff[0] = choice;
                buff[1] = n;
                printf("enter number to be searched: ");
                int t;
                scanf("%d", &t);
                buff[2] = t;
                res = send(s, buff, sizeof(arr), 0);
                if(res == -1){
                    close(s);
                    exit(0);
                }
                printf("\nParameters Sent Successfully");
                break;
            case 2:
                buff[0] = choice;
                buff[1] = n;  
                res = send(s, buff, sizeof(arr), 0);
                if(res == -1){
                    close(s);
                    exit(0);
                }
                break;
            case 3:
                buff[0] = choice;
                buff[1] = n;
                res = send(s, buff, sizeof(arr), 0);
                if(res == -1){
                    close(s);
                    exit(0);
                }
                break;
            case 4:
                buff[0] = choice;
                buff[1] = n;
                res = send(s, buff, sizeof(arr), 0);
                if(res == -1){
                    close(s);
                    exit(0);
                }
                break;
            case 5:
                buff[0] = choice;
                buff[1] = n;
                res = send(s, buff, sizeof(arr), 0);
                if(res == -1){
                    close(s);
                    exit(0);
                }
                break;
            default:
                printf("INVALID CHOICE..\n");
        }
    }
    close(s);
    exit(0);
}