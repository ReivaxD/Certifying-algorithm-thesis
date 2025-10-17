package CDCL;

public class CDCL {
    public static void main(String[] args) {
        Point p = new Point(1, 2);
        System.out.println(p);

        Point p2 = new Point(3, 2);
        Vector v = p.to(p2);
        System.out.println(v);

        double l = v.length();
        System.out.println(l);
    }
}
