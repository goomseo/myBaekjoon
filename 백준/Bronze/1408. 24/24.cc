#include <iostream>
using namespace std;

struct Time
{
    int hour;
    int min;
    int sec;
};

int main()
{

    Time now, deadline;

    int Sum(Time t);

    scanf("%02d:%02d:%02d", &now.hour, &now.min, &now.sec);
    scanf("%02d:%02d:%02d", &deadline.hour, &deadline.min, &deadline.sec);

    int nowSum = Sum(now);
    int deadlineSum = Sum(deadline);

    int temp = deadlineSum - nowSum;

    if (temp > 0)
    {
        printf("%02d:%02d:%02d", temp / 3600, temp % 3600 / 60, temp % 60);
    }
    else
    {
        temp += 24 * 3600;
        printf("%02d:%02d:%02d", temp / 3600, temp % 3600 / 60, temp % 60);
    }

    return 0;
}

int Sum(Time t)
{
    int sum = t.hour * 3600 + t.min * 60 + t.sec;

    return sum;
}