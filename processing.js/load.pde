String[] lines;
int[][] coord;

void setup(){
  size(1000,800);
  openFileChooser();
}

void openFileChooser(){
  selectInput("Select a RML/PATH file","fileSelected"); 
}

void fileSelected(File selection){
  if(selection == null){
   println("Window was closed."); 
  } else {
    String path = selection.getAbsolutePath();
    println("User selected "+ path); 
    lines = loadStrings(path);
    coord = new int[lines.length][2];
    for(int i=0;i<lines.length;i++){
        //println(lines[i]);
        String x = lines[i].split(" ")[0];
        String y = lines[i].split(" ")[1];
        print(x);
        print(":");
        print(y);
        println();
        coord[i][0] = int(x);
        coord[i][1] = int(y);    
    }
  }
  for(int i=0;i<coord.length;i++){
    print(coord[i][0]);
    print(":");
    print(coord[i][1]);
    println();
  }
}

int i = 0;
int x1,y1,x2,y2;
void draw(){
  if(coord!=null && i < coord.length-1){   
      x1=coord[i][0];
      y1=coord[i][1];
      x2=coord[i+1][0];
      y2=coord[i+1][1];
      //disp(x1,y1,x2,y2);      
    if(x2 == -1 || y2 == -1 ){
      i = i+2;
    } else {
      line(x1,y1,x2,y2);
      disp(x1,y1,x2,y2);      
      i ++;
    }
   println(i); 
   if(i>coord.length){
    while(true); 
   }

  }
}

void disp(int x1,int y1,int x2,int y2){
      print(x1);
      print(":");
      print(y1);
      print(":");
      print(x2);
      print(":");
      print(y2);
      println();
}
