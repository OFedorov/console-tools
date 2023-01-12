#include <termios.h>
#include <stdio.h>
#include <poll.h>
#include <unistd.h>
#include <stdlib.h>

#include "get_key.h"

char* get_key(){
    struct termios savetty;
    struct termios tty;
    char *ch = (char*) malloc(256);
    int i = 0;
    tcgetattr (0, &tty);
    savetty = tty;
    tty.c_lflag &= ~(ICANON|ECHO|ISIG);
    tty.c_cc[VMIN] = 1;
    tcsetattr (0, TCSAFLUSH, &tty);
    read(STDIN_FILENO, &(ch[i++]), 1);
    while (1) {
        struct pollfd pfd[1];
        pfd[0].fd = STDIN_FILENO;
        pfd[0].events = POLLIN;
        int ret = poll(pfd, 1, 0);
        if (ret == -1) {
            break;
        }
        if (!ret){
            break;
        }
        if (pfd[0].revents &POLLIN){
            read(STDIN_FILENO, &(ch[i++]), 1);
        }
    }
    ch[i] = 0;
    tcsetattr (0, TCSAFLUSH, &savetty);
    return ch;
}

