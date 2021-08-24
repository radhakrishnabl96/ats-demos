//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {4, 1, 0, 1.0};
//+
Point(3) = {3, 1, 0, 1.0};
//+
Point(4) = {3, 0.333, 0, 1.0};
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
Physical Surface("fluid", 11) = {1};
