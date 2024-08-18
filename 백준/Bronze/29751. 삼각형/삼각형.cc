#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int W, H;
	double result;
	cin >> W >> H;
	result = (W * H);
	result = result / 2;
	cout << fixed << setprecision(1) << result ;

	return 0;
}