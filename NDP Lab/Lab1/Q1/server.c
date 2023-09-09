#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<string.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<stdlib.h>


int main(){
    int s,r,sntb,recb;
    socklen_t len;
    int ca;
    int x;
    struct sockaddr_in server, client;
    printf("Input Port number: ");
    scanf("%d", &x);
    s = socket(AF_INET, SOCK_STREAM, 0);
    if(s == -1){
        printf("Error creating socket...\n");
        close(s);
        exit(0);
    }
    printf("socket created!!\n");
    server.sin_addr.s_addr = htonl(INADDR_ANY);
    server.sin_family = AF_INET;
    server.sin_port = htons(x);
    r = bind(s,(struct sockaddr*)&server, sizeof(server));
    if(r == -1){
        printf("Binding error...\n");
        close(s);
        exit(0);
    }
    printf("Socket Binded\n");
    r = listen(s,1);
    if(r == -1){
        close(s);
        exit(0);
    }
    printf("Socket Listening..\n");
    len = sizeof(client);
    int ns = accept(s, (struct sockaddr*)&client, &len);
    if(ns == -1){
        printf("Error Accepting..\n");
        close(s);
        exit(0);
    }
    printf("Socket Accepting..\n");
    char buff[50];
    int arr[10];
    int rec1 = recv(ns, arr, sizeof(arr), 0);
    if(rec1 < 0){
        printf("array receiving failed..\n");
        close(ns);
        exit(0);
    }
    printf("Array of numbers received: \n");
    int rec2;
    int opt = 0;
    while(opt!=5){
        rec1 = recv(ns, buff, sizeof(buff), 0);
        if(rec1 == -1){
            break;
        }
        printf("BUffer received \n");
        opt = buff[0];
        int n = buff[1];
        switch(opt){
            case 1:
                printf("\n");
                for(int i=0;i<n;i++){
                    if(arr[i] == buff[2]){
                        printf("FOUND AT INDEX %d\n", i);
                    }
                }
                break;

            case 2:
                printf("\n");
                printf("sorted in ascending order: \n");
                for(int i=0;i<n;i++){
                    for(int j = 0; j<n-i-1;j++){
                        if(arr[j] > arr[j+1]){
                            int temp;
                            temp = arr[j];
                            arr[j] = arr[j + 1];
                            arr[j + 1] = temp;
                        }
                    }
                }
                for(int i=0;i<n;i++){
                    printf(" %d ", arr[i]);
                }
                printf("\n");
                break;
            case 3:
                printf("\n");
                printf("sorted in ascending order: \n");
                for(int i=0;i<n;i++){
                    for(int j = 0; j<n-i-1;j++){
                        if(arr[j] < arr[j+1]){
                            int temp;
                            temp = arr[j];
                            arr[j] = arr[j + 1];
                            arr[j + 1] = temp;
                        }
                    }
                }
                for(int i=0;i<n;i++){
                    printf(" %d ", arr[i]);
                }
                printf("\n");
                break;
            case 4:
                printf("\n");
                printf("SPLITTING ARRAY\n");
                int arr1[10],arr2[10];
                int c1=0,c2=0;
                for(int i=0;i<n;i++){
                    if(arr[i]%2 == 0){
                        arr1[c1++] = arr[i];
                    }
                    else{
                        arr2[c2++] = arr[i];
                    }
                }
                printf("EVEN ARRAY\n");
                for(int i=0;i<c1;i++){
                    printf(" %d ", arr1[i]);
                }
                printf("\n");
                printf("ODD ARRAY\n");
                for(int i=0;i<c2;i++){
                    printf(" %d ", arr2[i]);
                }
                printf("\n");
                break;
            case 5:
                printf("EXITED\n");
                break;
            default:
                break;
                

        }
    }
    close(s);
    close(ns);
    exit(0);

}