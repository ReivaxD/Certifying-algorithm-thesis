package CDCL;

import java.util.ArrayList;

public class CDCL {
    public static void main(String[] args) {
        Point p0 = new Point(0, false);
        Point p1 = new Point(1, false);
        Point p2 = new Point(2, true);
        Point p3 = new Point(2, true);
        Point p4 = new Point(4, false);
        ArrayList<Point> points = new ArrayList<Point>();
        points.add(p0);
        points.add(p1);
        points.add(p2);
        points.add(p3);
        points.add(p4);

        ArrayList<Vecteur> vecteurs = new ArrayList<>();
        vecteurs.add(new Vecteur(p1, p2));
        vecteurs.add(new Vecteur(p3, p2));
        vecteurs.add(new Vecteur(p4, p3));
        vecteurs.add(new Vecteur(p1, p4));
        vecteurs.add(new Vecteur(p3, p4));

        Graph g = new Graph(vecteurs, points);
        g.reduce();
    }
}
