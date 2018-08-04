
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
char *builtin_str[] = {
  "cd",
  "help",
  "exit"
};


char *lsh_read_line(void)
{
  int size = 80;

  char *line = malloc(sizeof(char) * size);
  //int c;
  gets(line);
  return line;

}



char **lsh_split_line(char *line)
{
char *  tokens = strtok(line," ");
char **com=malloc(sizeof(tokens));
int i=0;
while( tokens != NULL )
   {
	com[i]=tokens;
        tokens = strtok(NULL, " ");
	i++;
   }

com[i]=NULL;
return com;


}
int shell_cd(char **args)
{
  if (args[1] == NULL) {
    fprintf(stderr, "shell: expected argument to \"cd\"\n");
  } else {
    if (chdir(args[1]) != 0) {
      perror("shell");
    }
  }
  return 1;
}



int shell_exit(char **args)
{
  return 0;
}



int  exe(char **com)
{ pid_t pid;
  if (com[0] == NULL) {
    // An empty command was entered.
    return 1;
  }
  if (strcmp(com[0], builtin_str[2]) == 0)
 {
 return 0;
 }
if (strcmp(com[0], builtin_str[0]) == 0)
 {shell_cd(com);

 return 1;

 }
pid = fork();

if(pid==0)
 {
execvp(com[0],com);

 }

 else{
 wait(0);

 }

return 1;
}





void loop(){
int c=1;
do{

printf("os_2017> ");
char *line=lsh_read_line();

    char **tokens=lsh_split_line(line);
    c= exe(tokens);
    //free(line);
   // free(tokens);
}while(c);


}


int main()
{
   printf("Welcome to OS class 2017 shell program\n");
   loop();
    return 0;

}
