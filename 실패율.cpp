#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>


using namespace std;

static bool cmp(pair<int, double>& a, pair<int, double>& b) {
	if(a.second == b.second)return a.first<b.first;
    else return a.second>b.second;
}


vector<int> solution(int N, vector<int> stages) {
	vector<int> answer;
    vector<pair<int,double>> save;
    int n[501]={0,};//스테이지에 있는 사람의 수 저장시키는 변수
    for(int i =0;i<stages.size();i++){
        n[stages[i]]++; //해당 스테이지 사람 수 증가 ++;
    }
    int people=stages.size();//푼사람 수 
    for(int i=1;i<=N;i++){     
        double per=0;
        if(n[i]>0){//0보다 크면 계산
        per=(double)n[i]/people;} 
        
        save.push_back({i,per});       
        people-=n[i];//탈락자 제거
    }
    sort(save.begin(),save.end(),cmp);
    for (auto num : save){//값 저장
        answer.push_back(num.first);
    }
	return answer;
}
