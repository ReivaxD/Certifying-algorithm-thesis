package CDCL;

class Vecteur {
    Point p1, p2;

    public Vecteur(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public boolean equals(Vecteur v){
        return (v.p1.equals(this.p1)) && (v.p2.equals(this.p2)) || (v.p1.equals(this.p2)) && (v.p2.equals(this.p1));
    }

    @Override
    public String toString() {
        return "(" + p1 + ", " + p2 + ")";
    }
}