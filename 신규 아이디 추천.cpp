#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
	string answer = "";
	//1단계
	bool h = 0;
	for (int i = 0; i < new_id.length(); i++) {
		int stack = 0;
		if (new_id[i] >= 'A' && new_id[i] <= 'Z') {
			new_id[i] += 32; h == false; stack = 0;
		}
		else if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')
			|| new_id[i] == '-' || new_id[i] == '_' ) {
			h == false; stack = 0;
		}
		else if (new_id[i] == '.') {
			stack++;
			if (i == 0) {
				h = true;
				continue;
			}
			if (stack > 1 && h == true) {
				continue;
			}
			if (stack == 1 && h == false) {
				answer += new_id[i];
				h = true;
				continue;
			}h = true;
		}
		else {
			continue;
		}
		answer += new_id[i];
	}
	return answer;
}
void main() {
	string new_id;
	cin >> new_id;
	cout << solution(new_id);
}
