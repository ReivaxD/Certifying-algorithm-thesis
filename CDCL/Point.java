package CDCL;

class Point {
    double number;
    boolean value;

    public Point(double number, boolean value) {
        this.number = number;
        this.value = value;
    }

    public Vecteur to(Point other) {
        return new Vecteur(new Point(number, value), other);
    }

    public boolean equals(Point p){
        return ((p.number == this.number) && (p.value == this.value));
    }

    @Override
    public String toString() {
        return "numero : " + number + ", Valeur : " + value;
    }
}