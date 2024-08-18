#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	string semina;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> semina;
		if (semina == "Algorithm") cout << 204 << endl;
		else if (semina == "DataAnalysis") cout << 207 << endl;
		else if (semina == "ArtificialIntelligence") cout << 302 << endl;
		else if (semina == "CyberSecurity") cout << "B101" << endl;
		else if (semina == "Network") cout << 303 << endl;
		else if (semina == "Startup") cout << 501 << endl;
		else if (semina == "TestStrategy") cout << 105 << endl;
	}
}