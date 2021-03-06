# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [ 
                # Définir ici les sommets
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],      
                [0, self.parameters['thickness'], 0],
                [0, self.parameters['thickness'],  self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], 0],
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                ]

        self.faces = [
                # définir ici les faces
                [0, 3, 2, 1],
                [0, 3, 6, 4],
                [2, 3, 6, 7],
                [6, 7, 5, 4],
                [1, 2, 7, 5],
                [1, 0, 4, 5]
                ]  
        
    # Draws the faces                
    def draw(self):        
        # A compléter en remplaçant pass par votre code
       for i in range (0,len(self.faces)-1):
          gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) # on trace les faces : GL_FILL
          gl.glPushMatrix()
          gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
          gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
          gl.glVertex3fv(self.vertices[self.faces[i][0]])
          gl.glVertex3fv(self.vertices[self.faces[i][1]])
          gl.glVertex3fv(self.vertices[self.faces[i][2]])
          gl.glVertex3fv(self.vertices[self.faces[i][3]])
          gl.glEnd()
          gl.glPopMatrix()