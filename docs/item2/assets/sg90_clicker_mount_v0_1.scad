// v0.2 hardware capsule: SG90 above ESP32-C3 SuperMini, hidden electronics, exposed USB-C + servo drive window. Soul intentionally omitted; only interface socket remains.
$fn=48;
mode="assembly"; // assembly, print_base, print_cover
module rounded_box(size=[10,10,10],r=2){minkowski(){cube([size[0]-2*r,size[1]-2*r,size[2]-2*r],center=true);sphere(r=r);}}
module sg90(){color("royalblue")translate([0,0,22]){rounded_box([23,12,24],1.4);translate([-15,0,0])rounded_box([10,12,19],1);translate([15,0,0])rounded_box([10,12,19],1);translate([0,0,15])cylinder(h=5,r=5,center=true);translate([0,0,19])cylinder(h=5,r=2.4,center=true);translate([-18,0,3])cube([6,15,3],center=true);translate([18,0,3])cube([6,15,3],center=true);}}
module esp32c3(){color("forestgreen")translate([0,0,5]){rounded_box([34,18,3],1);color("silver")translate([-20,0,0])cube([6,10,4],center=true);color("black")translate([2,0,2])cube([9,9,2],center=true);color("gold")translate([13,0,2])cube([9,14,1],center=true);for(x=[-12:4:14])for(y=[-10,10])color("gold")translate([x,y,2])cylinder(h=1.2,r=.8,center=true);}}
module wires(){for(i=[-1,0,1])color(i==-1?"saddlebrown":i==0?"red":"gold")translate([8,i*2,13])rotate([0,70,0])cylinder(h=28,r=.7,center=true);}
module base(){difference(){color("#222")translate([0,0,11])rounded_box([58,34,26],3);translate([-30,0,7])cube([13,13,9],center=true);translate([0,0,25])cube([30,18,15],center=true);}color("#555")translate([0,0,10])cube([40,22,2],center=true);}
module cover(){difference(){color("#111")translate([0,0,22])rounded_box([64,40,38],4);translate([0,0,7])cube([52,30,18],center=true);translate([-34,0,9])cube([12,16,9],center=true);translate([0,0,37])cube([31,20,14],center=true);}color("#333")translate([0,0,42])difference(){cylinder(h=4,r=12,center=true);cylinder(h=6,r=8,center=true);}}
module assembly(){base();esp32c3();wires();sg90();translate([0,0,4])%cover();}
if(mode=="assembly")assembly(); if(mode=="print_base")base(); if(mode=="print_cover")cover();
