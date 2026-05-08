
// SG90 + ESP32-C3 SuperMini Clicker Mount v0.1
// Units: millimeters
// Purpose: position a MicroServo 9g (SG90) so a short horn/lever can press a "click" target.
// This is a printable concept CAD source. Verify purchased SG90 and ESP32-C3 board dimensions before final print.

$fn = 48;

// ---- known / assumed dimensions ----
base_w = 90;
base_d = 70;
base_h = 3;

sg90_body_w = 23.0;      // left-right
sg90_body_d = 12.2;      // front-back
sg90_body_h = 29.0;      // vertical body
sg90_tab_w  = 32.5;
sg90_tab_d  = 4.0;
sg90_tab_h  = 2.5;
sg90_hole_d = 2.2;

esp_w = 22.5;
esp_d = 18.0;
esp_standoff_h = 5.0;
esp_hole_d = 1.6;

wall = 2.4;
clearance = 0.45;

module rounded_cube(size=[10,10,10], r=1.5){
  hull(){
    for(x=[r, size[0]-r]) for(y=[r, size[1]-r])
      translate([x,y,0]) cylinder(h=size[2], r=r);
  }
}

module base_plate(){
  difference(){
    rounded_cube([base_w, base_d, base_h], r=3);
    // four mounting holes
    for(x=[7, base_w-7]) for(y=[7, base_d-7])
      translate([x,y,-0.2]) cylinder(h=base_h+0.6, d=3.2);
  }
}

module sg90_body_mock(){
  color("#2563eb") translate([0,0,0]) cube([sg90_body_w, sg90_body_d, sg90_body_h]);
  color("#93c5fd") translate([(sg90_body_w-sg90_tab_w)/2, -sg90_tab_d, 17]) cube([sg90_tab_w, sg90_tab_d, sg90_tab_h]);
  color("#93c5fd") translate([(sg90_body_w-sg90_tab_w)/2, sg90_body_d, 17]) cube([sg90_tab_w, sg90_tab_d, sg90_tab_h]);
  color("white") translate([sg90_body_w/2, sg90_body_d/2, sg90_body_h]) cylinder(h=4, d=7);
}

module servo_cradle(){
  // SG90 body sits vertically in a U cradle, horn axis above body.
  sx = 18; sy = 18;
  difference(){
    union(){
      translate([sx-wall-clearance, sy-wall-clearance, base_h]) cube([wall, sg90_body_d+2*(wall+clearance), sg90_body_h+4]);
      translate([sx+sg90_body_w+clearance, sy-wall-clearance, base_h]) cube([wall, sg90_body_d+2*(wall+clearance), sg90_body_h+4]);
      translate([sx-wall-clearance, sy-wall-clearance, base_h]) cube([sg90_body_w+2*(wall+clearance), wall, 12]);
      translate([sx-wall-clearance, sy+sg90_body_d+clearance, base_h]) cube([sg90_body_w+2*(wall+clearance), wall, 12]);
      // tab support shelves
      translate([sx-6, sy-6, base_h+17-1.2]) cube([sg90_body_w+12, 3, 2.4]);
      translate([sx-6, sy+sg90_body_d+3, base_h+17-1.2]) cube([sg90_body_w+12, 3, 2.4]);
    }
    // M2-ish holes for SG90 tabs
    translate([sx+sg90_body_w/2-10, sy-6.2, base_h+18.2]) rotate([90,0,0]) cylinder(h=5, d=sg90_hole_d);
    translate([sx+sg90_body_w/2+10, sy-6.2, base_h+18.2]) rotate([90,0,0]) cylinder(h=5, d=sg90_hole_d);
    translate([sx+sg90_body_w/2-10, sy+sg90_body_d+6.2, base_h+18.2]) rotate([90,0,0]) cylinder(h=5, d=sg90_hole_d);
    translate([sx+sg90_body_w/2+10, sy+sg90_body_d+6.2, base_h+18.2]) rotate([90,0,0]) cylinder(h=5, d=sg90_hole_d);
  }
}

module esp32_mount(){
  // board shelf for USB/WiFi ESP32-C3 SuperMini, USB side faces outward.
  bx = 58; by = 15;
  color("#134e4a") translate([bx, by, base_h+esp_standoff_h]) cube([esp_w, esp_d, 1.6]);
  for(x=[0, esp_w]) for(y=[0, esp_d])
    translate([bx+x, by+y, base_h]) difference(){
      cylinder(h=esp_standoff_h, d=4.4);
      translate([0,0,-0.2]) cylinder(h=esp_standoff_h+0.4, d=esp_hole_d);
    }
  // cable strain relief bridge
  translate([bx-6, by+esp_d/2-4, base_h]) cube([5,8,6]);
}

module click_target(){
  // Reference target pad / key position, replace with actual keycap fixture if needed.
  translate([73, 42, base_h]) rounded_cube([12,9,5], r=1.5);
  translate([79, 46.5, base_h+5]) cylinder(h=1.2, d=7);
}

module servo_horn_reference(angle=28){
  // visual reference only; print separately if needed.
  translate([18+sg90_body_w/2,18+sg90_body_d/2,base_h+sg90_body_h+4]){
    cylinder(h=2, d=8);
    rotate([0,0,angle]) translate([0,-2.2,0]) rounded_cube([42,4.4,2], r=1.8);
    rotate([0,0,angle]) translate([38,-5,0]) rounded_cube([10,10,3], r=2);
  }
}

module assembly(){
  base_plate();
  servo_cradle();
  esp32_mount();
  click_target();
  %translate([18,18,base_h+1]) sg90_body_mock();
  %servo_horn_reference(28);
}

assembly();
