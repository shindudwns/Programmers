#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>


using namespace std;

static bool comp(pair<int, float>& a, pair<int, float>& b) {
	return a.second > b.second;
}
vector<int> solution(int N, vector<int> stages) {
	vector<int> answer;
	map<int, float> m;
	for (int i = 1; i <= N; i++) {
		float p=0, y=0; 
		for (int j = 0; j < stages.size(); j++) {
			if (stages[j] > i) {
				p++;
			}
			else if (stages[j] == i) {
				y++;
			}
		}float py = 0;
		if (p != 0 || p+y!=0)py = y / (p + y);
		m.insert(make_pair( i, py));
	}
	//sort(m.begin(), m.end(), cmp);
	vector<pair<int,float>> v(m.begin(), m.end());
	sort(v.begin(), v.end(), comp);
	for (auto num : v) {
        answer.push_back(num.first);
	}
	return answer;
}3,6,7,10~14,20,24 63
