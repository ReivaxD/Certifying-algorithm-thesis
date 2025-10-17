package CDCL;

class Point {
    double x, y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Vector to(Point other) {
        return new Vector(new Point(x, y), other);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}