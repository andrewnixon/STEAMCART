#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "SteamcartConfig.h"
#include "SteamArgParse.h"

int main (int argc, char *argv[])
{
  if (argc < 2)
    {
    helloWorld();
    return 1;
    }
  double inputValue = atof(argv[1]);
  double outputValue = sqrt(inputValue);
  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);
  return 0;
}
