import java.io.*;
import java.util.*;

public class MainD {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./16165.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, String[]> Group = new HashMap<>();
        Map<String, String> Member = new HashMap<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String group = st.nextToken();
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            String[] list = new String[n];
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                String member = st.nextToken();
                list[j] = member;
                Member.put(member, group);
            }
            Group.put(group, list);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String temp = st.nextToken();
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            if (t == 0) {
                String[] grouplist = Group.get(temp);
                Arrays.sort(grouplist);
                for (String value : grouplist) {
                    System.out.println(value);
                }
            } else {
                String member_group = Member.get(temp);
                System.out.println(member_group);
            }  
        }
    }
}
