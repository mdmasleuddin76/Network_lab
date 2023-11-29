#include <bits/stdc++.h>
using namespace std;
void generate(vector<vector<char>> &mat, string key)
{

    int arr[26] = {0}, k = 0, j = 0;
    for (int i = 0; i < key.size(); i++)
    {
        if (key[i] == 'j')
        {
            key[i] = 'i';
        }
        if (arr[key[i] - 'a'] == 0)
        {
            mat[j][k] = key[i];
            k++;
            if (k == 5)
            {
                j++;
                k = 0;
            }
            arr[key[i] - 'a'] = 1;
        }
    }
    for (char i = 'a'; i <= 'z'; i++)
    {
        if (i == 'j')
        {
            i++;
        }
        if (arr[i - 'a'] == 0)
        {
            mat[j][k] = i;
            k++;
            if (k == 5)
            {
                j++;
                k = 0;
            }
            arr[i - 'a'] = 1;
        }
    }
}
void search1(vector<vector<char>> mat, int &i1, int &j1, char temp)
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (mat[i][j] == temp)
            {
                i1 = i;
                j1 = j;
                return;
            }
        }
    }
}
void enycrypt(vector<vector<char>> mat, string &plaintext)
{
    if (plaintext.size() % 2)
        plaintext.push_back('x');

    for (int i = 0; i < plaintext.size(); i = i + 2)
    {
        char a = plaintext[i], b = plaintext[i + 1];
        if (plaintext[i] == plaintext[i + 1])
        {
            b = 'x';
        }
        int i1 = 0, i2 = 0, j1 = 0, j2 = 0;
        search1(mat, i1, j1, a);
        search1(mat, i2, j2, b);
        plaintext[i] = mat[i1][j2];
        plaintext[i + 1] = mat[i2][j1];
    }
}
void decrypt(string &plaintext)
{
    for (int i = 0; i < plaintext.size(); i++)
    {
        if (plaintext[i] == 'x' && 0 < i && i < plaintext.size() - 1)
            plaintext[i] = plaintext[i - 1];
    }
    if (plaintext[plaintext.size() - 1] == 'x')
        plaintext.pop_back();
}
int main()
{
    vector<vector<char>> mat(5, vector<char>(5, '0'));
    string str, key;
    bool flag = false;
     cout << "Enter the Plaintext" << endl;
     getline(cin, str);
    cout << "Enter the Key text" << endl;
    getline(cin, key);
    generate(mat, key);
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    while (1)
    {
        int opt = 0;
        cout << "Select an Option" << endl
             << "Enter 1 for Enycript" << endl
             << "Enter 2 for Dcrypt" << endl;
        cin >> opt;
        if (opt == 1)
        {
            if (flag)
            {
                cout << "Its already Enycrypted" << endl;
                cout << str << endl;
            }
            else
            {
                enycrypt(mat, str);
                cout << "Enycrptd string is" << endl;
                cout << str << endl;
                flag = true;
            }
        }
        else if (opt == 2)
        {
            if (flag == false)
            {
                cout << "Its already Decrypted" << endl;
                cout << str << endl;
            }
            else
            {
                enycrypt(mat, str);
                decrypt(str);
                cout << "Dycrptd string is" << endl;
                cout << str << endl;
                flag = false;
            }
        }
    }
}