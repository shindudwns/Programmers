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


//



#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
	string answer = "";
	//1단계
	bool h = false;
	for (int i = 0; i < new_id.length(); i++) {
		int stack = 0;
		if (new_id[i] >= 'A' && new_id[i] <= 'Z') {
			new_id[i] += 32; h = false; stack = 0;
		}
		else if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')
			|| new_id[i] == '-' || new_id[i] == '_') {
			h = false;
		}
		else if (new_id[i] == '.') {
			if (i == 0) {
				h = true;
				continue;
			}
			if (h == true) {
				continue;
			}
			h = true;
		}
		else {
			continue;
		}
		answer += new_id[i];
	}

	while (answer.length() > 15) {
		answer.erase(answer.length() - 1);
	}
	if (answer.length() > 0) {
		if (answer.back() == '.') answer.erase(answer.end() - 1);
	}
	else  {
		answer = "a";
	}
	if(answer.length()<3) {
		while (answer.length() < 3) {
			answer += answer[answer.length() - 1];
		}
	}
	return answer;
}
void main() {
	string new_id;
	cin >> new_id;
	cout << solution(new_id);
}
//


#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
	string answer = "";//입력값에서 출력값에 추가하여 구하는 형식
	bool h = false;//연속된 .인지 확인하는 변수
	for (int i = 0; i < new_id.length(); i++) { 
		if (new_id[i] >= 'A' && new_id[i] <= 'Z') {//대문자를 소문자로 변환
			new_id[i] += 32; h = false; 
		}
		else if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')
			|| new_id[i] == '-' || new_id[i] == '_') {
			h = false;//이에 해당된다면 연속.이 아니니 false함수 초기화
		}
		else if (new_id[i] == '.') {//.이 처음값은 패스 h값이 true이면 패스 해주는 조건문
			if (i == 0) {
				h = true;
				continue;
			}
			if (h == true) {
				continue;
			}
			h = true;
		}
		else {
			continue;
		}
		answer += new_id[i];//다 걸쳐지면 answer값에 저장
	}


	if(answer.length()==0) {//5단계
		answer = "a";
	}	
	if (answer.length() > 15) {
		while (answer.length() > 15) {
			answer.erase(answer.length() - 1);//6단계
		}
	}
	if (answer.length() > 0) {//6단계
		if (answer.back() == '.') answer.erase(answer.end() - 1);
	}
	if(answer.length()<3) {//7단계
		while (answer.length() < 3) {
			answer += answer[answer.length() - 1];
		}
	}
	return answer;
}
void main() {
	string new_id;
	cin >> new_id;
	cout << solution(new_id);
}
