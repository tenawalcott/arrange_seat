/*
Name: Arrange Seat
Author: Tena Walcott
Email: tenawalcott@gamil.com
*/
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
using namespace std;
const int MAXN=51;
int a[MAXN];
int n;
int get_rand(){
	int k=rand();
	if(a[(k+1)%n]==0)return (k+1)%n;
	else get_rand();
}
int main(){
	memset(a,0,sizeof(a));
	freopen("name.txt","r",stdin);
	cin>>n;
	fclose(stdin);
	srand(time(0));
	for(int i=1;i<=n;i++){
		int l=get_rand();
		a[l]=i;
	}
	freopen("random_list.txt","w",stdout);
	for(int i=0;i<n;i++)cout<<a[i]<<endl;
	fclose(stdout);
	return 0;
}
