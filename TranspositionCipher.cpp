#include <bits/stdc++.h>
using namespace std;
void Enycrypt(string &str, string key)
{
    cout << "Given String:-  " << str << endl;
    int n = str.length();
    int m = key.length();
    int row = n / m;
    if (n % m != 0)
    {
        row++;
    }
    char mat[row][m];
    int k = 0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (k < n)
            {
                mat[i][j] = str[k++];
            }
            else
            {
                mat[i][j] = ' ';
            }
        }
    }
    string temp = key;
    sort(temp.begin(), temp.end());
    str.clear();
    for (int i = 0; i < m; i++)
    {
        int index = 0;
        for (int k = 0; k < m; k++)
        {
            if (temp[i] == key[k])
            {
                key[k] = ' ';
                index = k;
                break;
            }
        }
        for (int j = 0; j < row; j++)
        {
            str.push_back(mat[j][index]);
        }
    }
    cout << "Encrypted String:-  " << str << endl;
}
void Decrypt(string &str, string key)
{
    cout << "Encrypted String:-  " << str << endl;
    int n = str.length();
    int m = key.length();
    int row = n / m;
    if (n % m != 0)
    {
        row++;
    }
    char mat[row][m];
    int k = 0;
    string temp = key;
    sort(temp.begin(), temp.end());
    for (int i = 0; i < m; i++)
    {
        int index = 0;
        for (int k = 0; k < m; k++)
        {
            if (temp[i] == key[k])
            {
                key[k] = ' ';
                index = k;
                break;
            }
        }
        for (int j = 0; j < row; j++)
        {
            mat[j][index] = str[k++];
        }
    }
    str.clear();
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < m; j++)
        {
            str.push_back(mat[i][j]);
        }
    }
    cout << "Decrypted String:-  " << str << endl;
}
int main()
{

    string str;
    cout << "Enter the string:-  ";
    getline(cin, str);
    string key;
    cout << "Enter the key:-  ";
    cin >> key;
    bool flag = false;
    while (1)
    {
        int option;
        cout << "1. Encrypt\n2. Decrypt\n3. Exit\n";
        cin >> option;
        if (option == 1)
        {
            flag = true;
            Enycrypt(str, key);
        }
        else if (option == 2)
        {
            if (!flag)
            {
                cout << "Please Encrypt the string first\n";
                continue;
            }
            Decrypt(str, key);
            flag = false;
        }
        else if (option == 3)
        {
            break;
        }
        else
        {
            cout << "Invalid Option\n";
        }
    }
    return 0;
}