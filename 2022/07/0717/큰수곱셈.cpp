#include <iostream>
#include <complex>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
typedef complex<double> cpx;
typedef long long ll;
const double PI = acos(-1);
int dp[10000];

void fft(vector<cpx>& A, bool inv = false) {
    int n = A.size(), j = 0;
    vector<cpx> roots(n / 2);
    for (int i = 1; i < n; i++) {
        int bit = (n >> 1);
        while (j >= bit) {
            j -= bit;
            bit >>= 1;
        }
        j += bit;
        if (i < j) swap(A[i], A[j]);
    }
    double ang = 2 * acos(-1) / n * (inv ? -1 : 1);
    for (int i = 0; i < n / 2; i++) {
        roots[i] = cpx(cos(ang * i), sin(ang * i));
    }
    for (int i = 2; i <= n; i <<= 1) {
        int step = n / i;
        for (int j = 0; j < n; j += i) {
            for (int k = 0; k < i / 2; k++) {
                cpx u = A[j + k], v = A[j + k + i / 2] * roots[step * k];
                A[j + k] = u + v;
                A[j + k + i / 2] = u - v;
            }
        }
    }
    if (inv) for (int i = 0; i < n; i++) A[i] /= n;
}
 
vector<ll> multiply(vector<ll>& v, vector<ll>& w) {
    vector<cpx> _A(v.begin(), v.end()), _B(w.begin(), w.end());
    int n = 2; 
    while (n < v.size() + w.size()) n <<= 1;
    _A.resize(n); 
    _B.resize(n);
    fft(_A, 0); 
    fft(_B, 0);
    for (int i = 0; i < n; i++) _A[i] *= _B[i];
    fft(_A, 1);
    vector<ll> C(n);
    for (int i = 0; i < n; i++) C[i] = (ll)round(_A[i].real());
    return C;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for (int i = 0; i < 10000;i++)
        dp[i] = i;
    freopen("text/15576.txt", "r", stdin);
    string a, b;
    cin >> a >> b;
    if (a == "0" || b == "0") {
        cout << 0 << "\n";
        return 0;
    }
    vector<ll> A(a.size()), B(b.size());
    for (int i = 0; i < a.size(); i++) A[a.size() - i - 1] = a[i] - '0';
    for (int i = 0; i < b.size(); i++) B[b.size() - i - 1] = b[i] - '0';

    vector<ll> C = multiply(A, B);
    for (int i = 0; i < a.size() + b.size() - 1; i++) {
        C[i + 1] += C[i] / 10;
        C[i] = C[i] % 10;
    }
    int cnt = C.size() - 1;
    while (C[cnt] == 0) {
        cnt--;
        if (cnt == 0) break;
    }
    for (int i = cnt; i >= 0; i--) cout << C[i];
    cout << "\n";
}
