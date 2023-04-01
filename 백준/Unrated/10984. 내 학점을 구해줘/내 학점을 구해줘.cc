#include <iostream>

using namespace std;

class Grades{
private:
    int courses;
    int credits[11] = {0};
    double grades[11] = {0};
public:
    Grades(int courses) {this -> courses = courses;}
    void read();
    int getCredits();
    double getGpa();
};

void Grades::read() {
    for (int i = 0; i < courses; i++)
        cin >> credits[i] >> grades[i];
}

int Grades::getCredits() {
    int sum = 0;
    for (int i = 0; i < courses; i++)
        sum += credits[i];

    return sum;
}

double Grades::getGpa() {
    double tmp = 0;
    for (int i = 0; i < courses; i++)
        tmp += credits[i] * grades[i];

    return tmp / (this -> getCredits());
}

int main(){
    int semesters;
    cin >> semesters;

    int courses;
    for (int i = 0; i < semesters; i++){
        cin >> courses;
        Grades grade(courses);

        grade.read();

        cout << grade.getCredits() << ' ';

        cout << fixed;
        cout.precision(1);
        cout << grade.getGpa() << endl;
    }
}