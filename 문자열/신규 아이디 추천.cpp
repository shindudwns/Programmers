#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
	string answer = "";//입력값에서 출력값에 추가하여 구하는 형식
	bool h = false;//연속된 .인지 확인하는 변수
	for (int i = 0; i < new_id.length(); i++) { 
		if (new_id[i] >= 'A' && new_id[i] <= 'Z') {//1단계
			new_id[i] += 32; h = false; 
		}
		else if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')
			|| new_id[i] == '-' || new_id[i] == '_') {
			h = false;//이에 해당된다면 연속.이 아니니 false함수 초기화
		}
		else if (new_id[i] == '.') {//.이 처음값은 패스 h값이 true이면 패스 해주는 조건문
			if (i == 0) {//4단계
				h = true;
				continue;
			}
			if (h == true) {//3단계
				continue;
			}
			h = true;
		}
		else {//2단계
			if (i == 0)
			{
				h = true;
			}
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
