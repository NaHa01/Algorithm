#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	string A, B;
	int over_10 = 0;
	int A_B = 0;
	string print;

	cin >> A >> B;

	int max_len = max(A.length(), B.length());
	A = string(max_len - A.length(), '0') + A;
	B = string(max_len - B.length(), '0') + B;

	for (int i = max_len - 1; i >= 0; i--) {
		A_B = (A[i] - '0') + (B[i] - '0') + over_10;
		over_10 = A_B / 10;
		print += (A_B % 10) + '0';
	}

	if (over_10 > 0) { print += over_10 + '0'; }

	reverse(print.begin(), print.end());

	cout << print;

	return 0;

}