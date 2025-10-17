package CDCL;
class Vector {
    Point p1, p2;

    public Vector(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public double length() {
        double l = Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
        System.out.println();
        return l;
    }

    @Override
    public String toString() {
        return "(" + p1 + ", " + p2 + ")";
    }
}