#include <iostream>
#include <complex>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
 
// Koosaga 팀노트 FFT 코드
using namespace std;
typedef complex<double> base;
typedef long long ll;
const double PI = acos(-1);
dp[10000000];

void fft(vector<base>& a, bool inv = false) {
    int n = a.size(), j = 0;
    vector<base> roots(n / 2);
    for (int i = 1; i < n; i++) {
        int bit = (n >> 1);
        while (j >= bit) {
            j -= bit;
            bit >>= 1;
        }
        j += bit;
        if (i < j) swap(a[i], a[j]);
    }
    double ang = 2 * acos(-1) / n * (inv ? -1 : 1);
    for (int i = 0; i < n / 2; i++) {
        roots[i] = base(cos(ang * i), sin(ang * i));
    }
    for (int i = 2; i <= n; i <<= 1) {
        int step = n / i;
        for (int j = 0; j < n; j += i) {
            for (int k = 0; k < i / 2; k++) {
                base u = a[j + k], v = a[j + k + i / 2] * roots[step * k];
                a[j + k] = u + v;
                a[j + k + i / 2] = u - v;
            }
        }
    }
    if (inv) for (int i = 0; i < n; i++) a[i] /= n;
}
 
vector<ll> multiply(vector<ll>& v, vector<ll>& w) {
    vector<base> A(v.begin(), v.end()), B(w.begin(), w.end());
    int n = 2; 
    while (n < v.size() + w.size()) n <<= 1;
    A.resize(n); 
    B.resize(n);
    fft(A, 0); 
    fft(B, 0);
    for (int i = 0; i < n; i++) A[i] *= B[i];
    fft(A, 1);
    vector<ll> ret(n);
    for (int i = 0; i < n; i++) ret[i] = (ll)round(A[i].real());
    return ret;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for (int i = 0; i < 10000000; i++) dp[i] = i;
    string str1, str2;
    cin >> str1 >> str2;
    if (str1 == "0" || str2 == "0") {
        cout << 0 << "\n";
        return 0;
    }
    vector<ll> a(str1.size()), b(str2.size());
    for (int i = 0; i < str1.size(); i++)a[str1.size() - i - 1] = str1[i] - '0';
    for (int i = 0; i < str2.size(); i++)b[str2.size() - i - 1] = str2[i] - '0';
    vector<ll> ret = multiply(a, b);
 
    for (int i = 0; i < str1.size() + str2.size() - 1; i++) {
        ret[i + 1] += ret[i] / 10;
        ret[i] = ret[i] % 10;
    }
    int cnt = ret.size() - 1;
    while (ret[cnt] == 0) {
        cnt--;
        if (cnt == 0) break;
    }
    for (int i = cnt; i >= 0; i--) cout << ret[i];
    cout << "\n";
}
