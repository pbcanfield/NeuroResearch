from bmtk.builder.auxi.node_params import positions_list
import numpy as np

def pos_EC():
    """Returns positions_list for EC Cells
    Original code: (MakeLocations.hoc:17)
        n=0
        for(y=0.25;y<=3;y+=0.5) {
            for(x=1.5;x<=15;x+=3) {
            z = 10
            locEC.x[0][n] = x
            locEC.x[1][n] = y	  
            locEC.x[2][n] = z
            n += 1
            }
        }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 1.5,15.5,3
    y_start, y_end, y_stride = 0.25,3,0.5
    z_start, z_end, z_stride = 10,11,1
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)

def pos_CA3e():
    """Returns positions_list for CA3e Cells (Principal Cells)
    Original code: (MakeLocations.hoc:60)
        n=0
        for(z=1;z<4;z+=1) {
            for(y=0.5;y<=3;y+=1) {
                for(x=0.5;x<=15;x+=2.3) {
                locCA3.x[0][n] = x
                locCA3.x[1][n] = y
                locCA3.x[2][n] = z		  
                
                n += 1
                }
            }
        }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 0.5,15,2.3
    y_start, y_end, y_stride = 0.5,3,1
    z_start, z_end, z_stride = 1,4,1
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)

def pos_CA3i():
    """Returns position_list for CA3i Cells (CA3 interneurons)
    // Interneurons
    Original code
        n=0
        for(z=1;z<4;z+=2) {
            for(y=0.75;y<=3;y+=1.5) {
                for(x=0.875;x<=7;x+=1.75) {
                    locCA3i.x[0][n] = x
                    locCA3i.x[1][n] = y
                    locCA3i.x[2][n] = z	

                    n += 1
                }
            }
        }
  """
  # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 0.875,7,1.75
    y_start, y_end, y_stride = 0.75,3,1.5
    z_start, z_end, z_stride = 1,4,2
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)

def pos_CA3o():
    """Returns positions_list for CA3o Cells (OLM Interneurons)
    Original code: (MakeLocations.hoc:32)
        n=0
        for(z=2;z<2.5;z+=2) {
            for(y=0.75;y<=3;y+=1.5) {
                for(x=1;x<=15;x+=4) {
                    locCA3o.x[0][n] = x
                    locCA3o.x[1][n] = y
                    locCA3o.x[2][n] = z	

                    n += 1
                }
            }
        }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 1,15,4
    y_start, y_end, y_stride = 0.75,3,1.5
    z_start, z_end, z_stride = 2,2.5,2
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)


def pos_CA3b():
    """Returns positions_list for CA3b Cells (Basket cell interneurons)
    Original code: (MakeLocations.hoc:46)
        n=0
        for(z=2;z<2.5;z+=2) {
            for(y=0.75;y<=3;y+=1.5) {
                for(x=1.5;x<=15;x+=4) {
                    locCA3b.x[0][n] = x
                    locCA3b.x[1][n] = y
                    locCA3b.x[2][n] = z	

                    n += 1
                }
            }
        }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 1.5,15,4
    y_start, y_end, y_stride = 0.75,3,1.5
    z_start, z_end, z_stride = 2,2.5,2
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)


def pos_DGg():
    """Returns positions_list for DGg Cells
    Original code: (MakeLocations.hoc:105)
    n=0
    for(z=5;z<8;z+=1) {
        for(y=0.47;y<=7.5;y+=0.94) {
            for(x=0.47;x<=15;x+=0.94) {
                locDG.x[0][n] = x
                locDG.x[1][n] = y
                locDG.x[2][n] = z	
                n += 1
            }
        }
    }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 0.47,15,0.94
    y_start, y_end, y_stride = 0.47,7.5,0.94
    z_start, z_end, z_stride = 5,8,1
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)


def pos_DGh():
    """Returns positions_list for DGh Cells
    Original code: (MakeLocations.hoc:17)
    n=0
    for(z=6;z<7;z+=1) {  
        for(y=0.9375;y<=7.5;y+=1.875) {
            for(x=0.8375;x<=15;x+=1.875) {
                //for(x=2;x<=15;x+=3.7) {
                locDGh.x[0][n] = x
                locDGh.x[1][n] = y
                locDGh.x[2][n] = z	
                n += 1
            }
        }
    }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 0.8375,15,1.875
    y_start, y_end, y_stride = 0.9375,7.5,1.875
    z_start, z_end, z_stride = 6,7,1
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)


def pos_DGb():
    """Returns positions_list for DGb Cells
    Original code: (MakeLocations.hoc:91)
    n=0
    for(z=6;z<7;z+=1) {  
        for(y=0.9375;y<=7.5;y+=1.875) {
            for(x=0.9375;x<=15;x+=1.875) {
                //    for(x=0.94;x<=15;x+=3.7) {
                locDGb.x[0][n] = x
                locDGb.x[1][n] = y
                locDGb.x[2][n] = z	
                n += 1
            }
        }
    }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 0.9375,15,1.875
    y_start, y_end, y_stride = 0.9375,7.5,1.875
    z_start, z_end, z_stride = 6,7,1
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)


def pos_DGi():
    """Returns positions_list for DG Interneuron Cells
    // Interneurons
    n=0
    for(z=5;z<8;z+=1) {
        for(y=0.9375;y<=7.5;y+=1.875) {
            for(x=0.9375;x<=15;x+=1.875) {
                locDGi.x[0][n] = x
                locDGi.x[1][n] = y
                locDGi.x[2][n] = z	
                n += 1
            }
        }
    }

    """
    # Create the possible x,y,z coordinates
    x_start, x_end, x_stride = 0.9375,15,1.875
    y_start, y_end, y_stride = 0.9375,7.5,1.875
    z_start, z_end, z_stride = 5,8,1
    x_grid = np.arange(x_start,x_end,x_stride)
    y_grid = np.arange(y_start,y_end,y_stride)
    z_grid = np.arange(z_start,z_end,z_stride)
    xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid)
    pos_list = np.vstack([xx.ravel(), yy.ravel(), zz.ravel()]).T
    
    return positions_list(pos_list)