#include<iostream>
#include<vector>
using namespace std;
void Solve(){
    int n;
    cin >> n;
    vector<int>a(n);
    vector<int>b(n);
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    for(int i=0;i<n;i++){
        cin >> b[i];
    }
    int om = 0 , andy = 0;
    int maxi = INT_MIN;
    for(int i = 0 ; i < n ; i++){
        if(a[i] == 0){
            maxi = max(maxi,om);
             om = 0;

        }
        else
        {
            om ++;
        }
    }
    int maxii = INT_MIN;
    for(int i = 0 ; i < n ; i++){
        if(b[i] == 0){
            maxii = max(maxii,andy);
            andy = 0;
        }
        else
        {
            andy ++;
        }
    }
    // cout << om << endl << andy;
    if(maxi > maxii){
        printf("Om\n");
    }
    else if(maxii > maxi){
        printf("Andy\n");
    }
    else
    {
        printf("Draw\n");
    }

}
int main(){
    int t;
    cin>>t;
    while(t--){
        Solve();
    }
    return 0;  
}