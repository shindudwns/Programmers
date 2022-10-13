#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string s) {
	int answer = s.size();
	for (int i = 1; i <= s.size() / 2; i++) {//최대 압축수가 길이의 반절이므로 반절까지 for문을 돌림.
		string zip_s = "";
		string copy_s = "";
		int stack = 0;//카운트 저장 스택변수
		copy_s = s.substr(0, i);//s문자열의 첫번재부터 압축갯수를 가르키는 i만큼 복사
		for (int j = i; j < s.size(); j += i) {//압축갯수만큼 for문을 돌려줌.
			if (copy_s == s.substr(j, i))  stack++; //돌리는것과 갯수가 같으면 갯수 증가
			else {
				if (stack > 0) { zip_s += to_string(stack+1); }//스택이 쌓였으면 숫자를 문자열에 추가
				zip_s += copy_s;//복사한 문자 추가
				copy_s = s.substr(j, i);// 압축할 문자 재지정
				stack = 0;//스택수 초기화
			}
		}
		if (stack > 0)  zip_s += to_string(stack+1); 
		zip_s += copy_s;
		//if (isdigit(zip_s[0])) 
		if (answer > zip_s.size()) answer = zip_s.size();
		//더 작은값 저장
	}
	return answer;
}
#33
