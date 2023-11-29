
#include <bits/stdc++.h>
using namespace std;
void decrypt(string &text, int key)
{
    cout << "Encrypted String:-  " << text << endl;
    for (int i = 0; i < text.length(); i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            int temp = text[i] - 'a';
            temp = (temp - key) % 26;
            if (temp < 0)
            {
                temp = temp + 26;
            }
            text[i] = temp + 'a';
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            int temp = text[i] - 'A';
            temp = (temp - key) % 26;
            if (temp < 0)
            {
                temp = temp + 26;
            }
            text[i] = temp + 'A';
        }
    }
    cout << "Decrypted String:-  " << text << endl;
}
void enycrypt(string &text, int key)
{
    cout << "Given String:-  " << text << endl;
    for (int i = 0; i < text.length(); i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            int temp = text[i] - 'a';
            temp = (temp + key) % 26;
            text[i] = temp + 'a';
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            int temp = text[i] - 'A';
            temp = (temp + key) % 26;
            text[i] = temp + 'A';
        }
    }
    cout << "Encrypted String:-  " << text << endl;
}
int main()
{
    string text;
    cout << "Enter the string:-  ";
    getline(cin, text);
    int key;
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
            enycrypt(text, key);
        }
        else if (option == 2)
        {
            if (!flag)
            {
                cout << "Please Encrypt the string first\n";
                continue;
            }
            decrypt(text, key);
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