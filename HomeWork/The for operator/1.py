int main()
{
int x, y, res = 1;
cin >> x >> y;
for (int i = 0; i < y; ++i)
res *= x;
cout << res;
return 0;
}