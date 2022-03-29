#include<stdio.h>
int main()
{
    float R,H,h;
    float pi=(float)22/7;
    scanf("%f",&R);
    scanf("%f",&H);
    scanf("%f",&h);
    float V1,V2,V3;
    V1= (pi*R*R*H);
    V2=((2*pi*R*R*R)/3);
    V3=((pi*R*R*h)/3);
    printf("%f",V1-V2-V3);
    }