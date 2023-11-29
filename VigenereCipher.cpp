#include <bits/stdc++.h>
using namespace std;
void Table(char table[26][26])
{
    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            table[i][j] = (i + j) % 26 + 'A';
        }
    }
}
void Enycrypt(string &text, string key, char table[26][26])
{
    cout << "Given String:-  " << text << endl;
    for (int k = 0; k < text.size(); k++)
    {
        int i = text[k] - 'A', j = key[k] - 'A';
        if (text[k] >= 'A' && 'Z' >= text[k])
        {
            text[k] = table[i][j];
        }
    }
    cout << "Encrypted String:-  " << text << endl;
}
void Decrypt(string &text, string key, char table[26][26])
{
    cout << "Encrypted String:-  " << text << endl;

    for (int k = 0; k < text.size(); k++)
    {
        int j = key[k] - 'A';
        if (text[k] >= 'A' && 'Z' >= text[k])
        {
            for (int i = 0; i < 26; i++)
            {
                if (table[i][j] == text[k])
                {
                    text[k] = i + 'A';
                    break;
                }
            }
        }
    }
    cout << "Decrypted String:-  " << text << endl;
}
int main()
{
    string text;
    cout << "Enter the string:-  ";
    getline(cin, text);
    string key;
    cout << "Enter the key:-  ";
    cin >> key;
    string temp = key;
    while (key.size() < text.size())
        key += temp;
    bool flag = false;
    char table[26][26];
    Table(table);
    for(int i=0;i<text.size();i++){
        if(text[i]>='a'&&text[i]<='z'){
            text[i]=text[i]-'a'+'A';
        }
    }
    for(int i=0;i<key.size();i++){
        if(key[i]>='a'&&key[i]<='z'){
            key[i]=key[i]-'a'+'A';
        }
    }
    while (1)
    {
        int option;
        cout << "1. Encrypt\n2. Decrypt\n3. Exit\n";
        cin >> option;
        if (option == 1)
        {
            flag = true;
            Enycrypt(text, key, table);
        }
        else if (option == 2)
        {
            if (!flag)
            {
                cout << "Please Encrypt the string first\n";
                continue;
            }
            Decrypt(text, key, table);
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
}