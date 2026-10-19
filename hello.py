print("Hello GitHub!")
# Kiran Thawre
BTech CSE (AIML) student, Cummins College of Engineering for Women, Nagpur
Skills: C, C++, Java, Python

#C language 
include<stdio.h>
int main()
{
  int a;
  printf ("Enter a variable");
  scanf ("%d",a);
  return 0;
}

#C++
#include <iostream>
using namespace std;
int main() {
    cout << "Hello GitHub!";
    return 0;

}

#java 

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello GitHub!");
    }
}

#C language
 
#include <stdio.h>
#include <limits.h>

int main() {
    int a[] = {12, 35, 1, 10, 34, 1};
    int n = 6, first = INT_MIN, second = INT_MIN;
    for (int i = 0; i < n; i++) {
        if (a[i] > first) { second = first; first = a[i]; }
        else if (a[i] > second && a[i] != first) second = a[i];
    }
    printf("Second largest = %d\n", second);
    return 0;
}


#C++

#include <iostream>
#include <climits>
using namespace std;

int main() {
    int a[] = {12, 35, 1, 10, 34, 1};
    int n = 6, first = INT_MIN, second = INT_MIN;
    for (int i = 0; i < n; i++) {
        if (a[i] > first) { second = first; first = a[i]; }
        else if (a[i] > second && a[i] != first) second = a[i];
    }
    cout << "Second largest = " << second << endl;
    return 0;
}

#JAVA 

public class SecondLargest {
    public static void main(String[] args) {
        int[] a = {12, 35, 1, 10, 34, 1};
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
        for (int x : a) {
            if (x > first) { second = first; first = x; }
            else if (x > second && x != first) second = x;
        }
        System.out.println("Second largest = " + second);
    }
}

#Python 

a = [12, 35, 1, 10, 34, 1]
first = second = float('-inf')
for x in a:
    if x > first:
        second, first = first, x
    elif x > second and x != first:
        second = x
print("Second largest =", second)