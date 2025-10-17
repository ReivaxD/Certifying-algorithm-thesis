package CDCL;

import java.util.ArrayList;

public class Graph {
    ArrayList<Vecteur> vecteurs;
    ArrayList<Point> points;

    public Graph(ArrayList<Vecteur> vecteurs, ArrayList<Point> points){
        this.vecteurs = vecteurs;
        this.points = points;
    }

    public void addPoint(Point p){
        points.add(p);
    }

    public void addVecteur(Vecteur v){
        vecteurs.add(v);
    }

    public void delPoint(Point p){
        points.remove(p);
    }

    public void delVecteur(Vecteur v){
        vecteurs.remove(v);
    }

    public void reduce(){
        int ip = 0;
        int iv = 0;
        ArrayList<Point> doublepoint = new ArrayList<Point>();
        ArrayList<Point> copypoints = (ArrayList<Point>) points.clone();
        for (Point point : copypoints) {
            for (Point point2 : copypoints) {
                if(point.equals(point2) && (point != point2) && !(doublepoint.contains(point))){
                    points.remove(point2);
                    ip++;
                    doublepoint.add(point2);
                }
            }
        }
        ArrayList<Vecteur> doublevecteur = new ArrayList<Vecteur>();
        ArrayList<Vecteur> copyvecteurs = (ArrayList<Vecteur>) vecteurs.clone();
        for (Vecteur vecteur : copyvecteurs) {
            for (Vecteur vecteur2 : copyvecteurs){
                if(vecteur.equals(vecteur2) && (vecteur != vecteur2) && !(doublevecteur.contains(vecteur))){
                    vecteurs.remove(vecteur2);
                    iv++;
                    doublevecteur.add(vecteur2);
                }
            }
        }
    System.out.println(ip + " point(s) supprimes");
    System.out.println(iv + " vecteur(s) supprimes");
    }
}
