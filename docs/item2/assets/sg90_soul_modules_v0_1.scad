// SG90 SOUL Modules v0.1
// Interchangeable lightweight modules for the SG90 hardware capsule top socket.
$fn=48;
mode="plate"; // plate, gemini, claude, openai, grok, clawd, openclaw
module soul_adapter_base(){
  difference(){
    union(){cylinder(h=4,r=12);translate([0,0,4])cylinder(h=2,r=9);} // mates Ø24/Ø16 socket reference
    translate([0,0,-1])cylinder(h=8,r=2.2); // SG90 horn screw access
    translate([0,0,1])cylinder(h=4,r=8); // horn clearance cavity
  }
}
module fin(points,h=18,thick=2){linear_extrude(height=thick)polygon(points);}
module gemini(){soul_adapter_base();color("cyan"){translate([-5,-1,6])fin([[0,8],[4,0],[0,-8],[-4,0]],22,2);translate([5,1,6])fin([[0,8],[4,0],[0,-8],[-4,0]],22,2);}}
module claude(){soul_adapter_base();color("orange")translate([-5,-2,6])minkowski(){cube([10,4,22]);sphere(1.5);}}
module openai(){soul_adapter_base();color("white")for(a=[0:60:300])rotate([0,0,a])translate([6,0,7])rotate([90,0,0])cylinder(h=3,r=5,center=true);}
module grok(){soul_adapter_base();color("yellow")translate([-3,-1,6])fin([[-3,13],[5,2],[1,2],[6,-12],[-6,-1],[-1,-1]],24,2.5);}
module clawd(){soul_adapter_base();color("#8b5cf6"){translate([-5,0,7])rotate([0,0,22])cube([3,16,16],center=true);translate([5,0,7])rotate([0,0,-22])cube([3,16,16],center=true);}}
module openclaw(){soul_adapter_base();color("#22d3ee")translate([0,0,13])cube([16,5,12],center=true);color("black")translate([-4,-3,16])sphere(1.2);color("black")translate([4,-3,16])sphere(1.2);}
if(mode=="plate")soul_adapter_base();
if(mode=="gemini")gemini(); if(mode=="claude")claude(); if(mode=="openai")openai(); if(mode=="grok")grok(); if(mode=="clawd")clawd(); if(mode=="openclaw")openclaw();
