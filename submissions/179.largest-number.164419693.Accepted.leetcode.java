public class Solution
{
    public String largestNumber(int[] nums)
    {
        StringBuilder result = new StringBuilder();
        List<Integer> datas = new ArrayList<Integer>();

        for (int i : nums)
        {
            datas.add(i);
        }

        Collections.sort(datas, new Comparator<Integer>()
        {
            public int compare(Integer o1, Integer o2)
            {
                return (o2 + "" + o1).compareTo(o1 + "" + o2);
            }
        });

        for (int nav = 0; nav < datas.size(); nav++)
        {
            result.append(datas.get(nav));
        }

        return result.toString().replaceFirst("^0+(?!$)", "");
    }
}


