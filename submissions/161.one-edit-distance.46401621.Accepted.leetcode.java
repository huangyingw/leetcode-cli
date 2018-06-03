public class Solution
{
    public boolean isOneEditDistance(String s, String t)
    {
        int m = s.length(), n = t.length();

        if (m > n)
        {
            return isOneEditDistance(t, s);
        }

        int i = 0, shift = n - m;

        if (shift > 1)
        {
            return false;
        }

        while (i < m && s.charAt(i) == t.charAt(i))
        {
            ++i;
        }

        if (i == m)
        {
            return shift > 0;
        } // if two string are the same (shift==0), return false

        if (shift == 0)
        {
            i++;
        } // if n==m skip current char in s (modify operation in s)

        while (i < m && s.charAt(i) == t.charAt(i + shift))
        {
            i++;
        } // use shift to skip one char in t

        return i == m;
    }
}

