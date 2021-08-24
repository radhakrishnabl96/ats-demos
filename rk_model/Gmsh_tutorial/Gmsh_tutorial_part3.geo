h1 = 0.1;
//+
Point(1) = {0, 0, 0, h1};
//+
Point(2) = {4, 1, 0, 1.0};
//+
Point(3) = {3, 1, 0, 1.0};
//+
Point(4) = {3, 0.333, 0, 2*h1};
//+
Point(5) = {0, 0.333, 0, 1.0};
//+
Point(6) = {0, 4, 0, 1.0};
//+
Point(7) = {4, 0, 0, 1.0};
//+
Line(1) = {1, 7};
//+
Line(2) = {7, 2};
//+
Line(3) = {2, 3};
//+
Line(4) = {3, 4};
//+
Line(5) = {4, 5};
//+
Line(6) = {1, 5};
//+
Curve Loop(1) = {5, -6, 1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Physical Curve("inlet", 7) = {6};
//+
Physical Curve("outlet", 8) = {3};
//+
Physical Curve("wall_out", 9) = {1, 2};
//+
Physical Curve("wall_in", 10) = {5, 4};
//+
Transfinite Curve {5} = 25 Progression 1/1.2;
//+
Field[1] = Cylinder;
//+
Field[1].Radius = 0.25;
//+
Field[1].VIn = 0.05;
//+
Field[1].VOut = 1;
//+
Field[1].XAxis = 1;
//+
Field[1].XCenter = 1;
//+
Field[1].YCenter = 0.5;
//+
Field[1].XCenter = 1;
//+
Field[1].Radius = 0.1;
//+
Field[1].YCenter = 0.1;
