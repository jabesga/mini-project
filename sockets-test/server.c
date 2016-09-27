#include <stdio.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

void error(char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
     // check argument
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     int socketfd, newsocket, portno, clilen;

     portno = atoi(argv[1]);

     char buffer[256];
     struct sockaddr_in serv_addr, cli_addr;
     int n;

     socketfd = socket(AF_INET, SOCK_STREAM, 0);
     if (socket < 0) 
        error("ERROR opening socket");

     bzero((char *) &serv_addr, sizeof(serv_addr));

     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);


     if (bind(socketfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0) 
              error("ERROR on binding");

     listen(socketfd,5);
     clilen = sizeof(cli_addr);
     newsocket = accept(socketfd, (struct sockaddr *) &cli_addr, &clilen);
     if (newsocket < 0) 
          error("ERROR on accept");
     bzero(buffer,256);
     n = read(newsocket,buffer,255);
     if (n < 0) error("ERROR reading from socket");
     printf("Here is the message: %s\n",buffer);
     n = write(newsocket,"I got your message",10);
     if (n < 0) error("ERROR writing to socket");
     return 0; 
}
