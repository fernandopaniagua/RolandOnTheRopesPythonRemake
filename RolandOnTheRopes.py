#
# Mi pequenyo homenaje a los heroes que programaron tan maravillosos juegos con tanto trabajo
# y talento.
#
# Mis disculpas para quellos que quieran entender el codigo y no lo consigan. Esta programado
# un poco a lo loco, solo para ver que daba de si Pygame :)
# 
# Los graficos estan hechos a partir de los originales o son originales (los menos).
# Roland (Fred) es el del original, obtenido mediante capturas de pantalla.
#
# Los sonidos estan descargados de freesound.org:
# 	success.wav es obra de grunz https://freesound.org/people/grunz/sounds/109662/
# 	collect.wav es obra de Wagna https://freesound.org/people/Wagna/sounds/325805/
# 	step.wav es obra de RandomationPictures https://freesound.org/people/RandomationPictures/sounds/138476/ 
#	error.wav es obra de Raclure https://freesound.org/people/Raclure/sounds/405548/
#	friction.wav es obra de josepharaoh99 https://freesound.org/people/josepharaoh99/sounds/389590/
#
# By Fernando Paniagua (2018)
# fernando.paniagua@gmail.com
#
# Alcorcon, Madrid, Spain, 1 de Mayo de 2018
#
# Version Python: 3.6.5.
#
# Nota: No hay tildes en la documentacion porque el interprete de Python version 2 protestaba.
# Nota: si hay gamepad no funciona el teclado. Probado con 8Bitdo
#

import pygame
import sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
pygame.joystick.init()

#Window size
windowWidth = 640
windowHeight = 400
window = pygame.display.set_mode((windowWidth, windowHeight))

#Color o verde?
CPC_GREEN = "cpc_green"
CPC_COLOR = "cpc_color"

#Pantallas
screenStyle = pygame.image.load("screens/select_style.png")

#Estado del juego
estado_juego = 0 #0 seleccion estilo; 1 portada; 2 jugando; 3 final

#Reloj del juego
reloj = pygame.time.Clock()

#Tiempo inicial del juego
startTick = pygame.time.get_ticks()

#Tiempo de espera durante la (fake) carga 
loadingTime=3000

while estado_juego!=2:
	#Ritmo del juego
	reloj.tick(60)

	#Background color - Clear window
	window.fill((0,0,0))

	if estado_juego==0:
		window.blit(screenStyle,(0,0))
		for event in GAME_EVENTS.get():
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_1:
					estado_juego=1
					colorStyle = CPC_COLOR
					screenPortada = pygame.image.load("screens/" + colorStyle + "/portada.png")
				elif event.key == pygame.K_2:
					estado_juego=1
					colorStyle = CPC_GREEN
					screenPortada = pygame.image.load("screens/" + colorStyle + "/portada.png")
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
	
	elif estado_juego==1:
		window.blit(screenPortada,(0,0))

		if (pygame.time.get_ticks()>(startTick+loadingTime)):
			estado_juego=2
		
		for event in GAME_EVENTS.get():
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				else:
					estado_juego=2

	pygame.display.update()


#Assets
bloque1 = pygame.image.load("images/" + colorStyle + "/bloque.png")
bloque2 = pygame.image.load("images/" + colorStyle + "/bloque2.png")
bloqueLampara1 = pygame.image.load("images/" + colorStyle + "/bloque_lampara1.png")
bloqueLampara2 = pygame.image.load("images/" + colorStyle + "/bloque_lampara2.png")
bloqueArgolla = pygame.image.load("images/" + colorStyle + "/bloque_argolla.png")
cuerdaNudo = pygame.image.load("images/" + colorStyle + "/cuerda_nudo.png")
cuerdaCentro = pygame.image.load("images/" + colorStyle + "/cuerda_centro.png")
cuerdaExtremo = pygame.image.load("images/" + colorStyle + "/cuerda_extremo.png")
sky = pygame.image.load("images/" + colorStyle + "/sky.png")
moon = pygame.image.load("images/" + colorStyle + "/moon.png")
suelo = pygame.image.load("images/" + colorStyle + "/suelo.png")
salida = pygame.image.load("images/" + colorStyle + "/salida.png")
gameover = pygame.image.load("images/" + colorStyle + "/gameover.png")
creditos1 = pygame.image.load("images/" + colorStyle + "/creditos1.png")

llave0 = pygame.image.load("images/" + colorStyle + "/llave0.png")
llave1 = pygame.image.load("images/" + colorStyle + "/llave1.png")
llave2 = pygame.image.load("images/" + colorStyle + "/llave2.png")
llave3 = pygame.image.load("images/" + colorStyle + "/llave3.png")

gota00 = pygame.image.load("images/" + colorStyle + "/gotas/gota00.png")
gota0 = pygame.image.load("images/" + colorStyle + "/gotas/gota0.png")
gota1 = pygame.image.load("images/" + colorStyle + "/gotas/gota1.png")
gota2 = pygame.image.load("images/" + colorStyle + "/gotas/gota2.png")
gota3 = pygame.image.load("images/" + colorStyle + "/gotas/gota3.png")
gota4 = pygame.image.load("images/" + colorStyle + "/gotas/gota4.png")
gota5 = pygame.image.load("images/" + colorStyle + "/gotas/gota5.png")
gota6 = pygame.image.load("images/" + colorStyle + "/gotas/gota6.png")
gota7 = pygame.image.load("images/" + colorStyle + "/gotas/gota7.png")
gota8 = pygame.image.load("images/" + colorStyle + "/gotas/gota8.png")
gota9 = pygame.image.load("images/" + colorStyle + "/gotas/gota9.png")
gota10 = pygame.image.load("images/" + colorStyle + "/gotas/gota10.png")
gota11 = pygame.image.load("images/" + colorStyle + "/gotas/gota11.png")
gota12 = pygame.image.load("images/" + colorStyle + "/gotas/gota12.png")
gota13 = pygame.image.load("images/" + colorStyle + "/gotas/gota13.png")
gota14 = pygame.image.load("images/" + colorStyle + "/gotas/gota14.png")
gota15 = pygame.image.load("images/" + colorStyle + "/gotas/gota15.png")
gota16 = pygame.image.load("images/" + colorStyle + "/gotas/gota16.png")
gota17 = pygame.image.load("images/" + colorStyle + "/gotas/gota17.png")
gota18 = pygame.image.load("images/" + colorStyle + "/gotas/gota18.png")
gota19 = pygame.image.load("images/" + colorStyle + "/gotas/gota19.png")
gota20 = pygame.image.load("images/" + colorStyle + "/gotas/gota20.png")
gota21 = pygame.image.load("images/" + colorStyle + "/gotas/gota21.png")
gota22 = pygame.image.load("images/" + colorStyle + "/gotas/gota22.png")
gota23 = pygame.image.load("images/" + colorStyle + "/gotas/gota23.png")
gota24 = pygame.image.load("images/" + colorStyle + "/gotas/gota24.png")
gota25 = pygame.image.load("images/" + colorStyle + "/gotas/gota25.png")
gota26 = pygame.image.load("images/" + colorStyle + "/gotas/gota26.png")
gota27 = pygame.image.load("images/" + colorStyle + "/gotas/gota27.png")
gota28 = pygame.image.load("images/" + colorStyle + "/gotas/gota28.png")

#Sonidos
pasos = pygame.mixer.Sound("sounds/step.wav")
friction = pygame.mixer.Sound("sounds/friction.wav")
collect = pygame.mixer.Sound("sounds/collect.wav")
error = pygame.mixer.Sound("sounds/error.wav")
success = pygame.mixer.Sound("sounds/success.wav")

#Dimensiones
ancho_bloque = 104
alto_bloque = 84.0

#ROLAND
roland0 = pygame.image.load("images/" + colorStyle + "/roland0.png")
roland1 = pygame.image.load("images/" + colorStyle + "/roland1.png")
roland2 = pygame.image.load("images/" + colorStyle + "/roland2.png")
roland3 = pygame.image.load("images/" + colorStyle + "/roland3.png")
roland4 = pygame.image.load("images/" + colorStyle + "/roland4.png")
roland5 = pygame.image.load("images/" + colorStyle + "/roland5.png")
roland6 = pygame.image.load("images/" + colorStyle + "/roland6.png")
roland7 = pygame.image.load("images/" + colorStyle + "/roland7.png")
roland = [roland0, roland1, roland2, roland3, roland4, roland5, roland6, roland7]
step = 0 #frame de Roland a mostrar en cada momento
limiteDeltaStep = 10 #tiempo entre animaciones
deltaStep = limiteDeltaStep-1 #tiempo desde la ultima animacion, se inicializa a limiteDeltaStep-1 para que comience a animar desde el principio
rolandXSpeed=3.5 #velocidad de Roland en el eje X
rolandYSpeed=2 #velocidad de Roland en el eje Y
rx=(ancho_bloque*2)#x de Roland
ry=(windowHeight-alto_bloque*3)#y de Roland

#Movimiento
deltaX=ancho_bloque*4*-1 #delta de la coordenada X, mueve la pantalla
deltaY=0 #delta de la coordenada Y, mueve la pantalla

#Estado del teclado
estado=0 #0 pausa, 1 derecha, 2 izquierda, 3 arriba, 4 abajo (Python tiene constantes?)

#Constantes
TIEMPO_PARPADEO=150 #Tiempo entre cada parpadeo de las linternas
TIEMPO_PARPADEO_GOTA_NORMAL=40
TIEMPO_PARPADEO_GOTA_PAUSA=400
tiempo_parpadeo_gota=TIEMPO_PARPADEO_GOTA_NORMAL #Tiempo entre frame del goteo verde
CORRECCION_CUERDA=16 #pixeles que se modifica la posicion de Roland para que agarre la cuerda
MARGEN_SEGURIDAD=18 #Margen de seguridad para no darse con la cabeza en el techo ni con los pies en el suelo al subir/bajar de la cuerda

#Blocks position
mapa = [
	[suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo,suelo],
	[suelo,suelo,bloque1,bloqueLampara1,bloque2,bloque1,bloqueArgolla,bloqueLampara2,bloque2,bloque1,bloqueLampara1,bloqueArgolla,bloqueLampara2,bloque2,suelo,suelo,suelo],
	[suelo,suelo,bloque1,cuerdaExtremo,None,bloque1,None,gota1,None,cuerdaExtremo,None,bloqueArgolla,cuerdaExtremo,bloqueArgolla,suelo,suelo,suelo],
	[suelo,suelo,bloqueLampara1,cuerdaCentro,bloque1,bloque1,bloque2,bloque1,bloque2,cuerdaCentro,bloque1,bloque2,cuerdaCentro,bloque1,suelo,suelo,suelo],
	[suelo,suelo,bloqueArgolla,cuerdaNudo,cuerdaExtremo,bloque2,None,cuerdaExtremo,bloqueLampara1,cuerdaCentro,bloque2,cuerdaExtremo,cuerdaNudo,bloque2,suelo,suelo,suelo],
	[suelo,suelo,bloque1,bloque1,cuerdaCentro,bloqueArgolla,bloque2,cuerdaCentro,None,cuerdaNudo,None,cuerdaCentro,bloque1,bloqueArgolla,suelo,suelo,suelo],
	[suelo,suelo,bloque1,cuerdaExtremo,cuerdaNudo,None,None,cuerdaNudo,bloque2,bloqueArgolla,bloque1,cuerdaCentro,llave0,bloque1,suelo,suelo,suelo],
	[suelo,suelo,bloque1,cuerdaCentro,bloque1,bloqueLampara1,bloque1,bloque2,bloque1,cuerdaExtremo,None,cuerdaNudo,bloqueLampara1,bloque1,suelo,suelo,suelo],
	[suelo,suelo,bloque1,cuerdaNudo,None,gota3,None,cuerdaExtremo,bloqueArgolla,cuerdaNudo,bloque1,bloque2,bloque1,bloque1,suelo,suelo,suelo],
	[suelo,suelo,bloque1,bloque1,bloque1,bloque1,bloque1,salida,bloque1,bloque1,bloque1,bloque1,bloque1,bloque1,suelo,suelo,suelo],
	[sky,sky,creditos1,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,gameover,sky,sky,sky],
	[sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky],
	[sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,sky,moon,sky,sky]
]

#Listas de elementos
solidos = [bloque1,bloque2,bloqueArgolla,bloqueLampara1,bloqueLampara2,gameover,creditos1]
cuerdas = [cuerdaExtremo,cuerdaCentro,cuerdaNudo]
llaves = [llave0, llave1, llave2, llave3]
gotas = [gota00,gota0,gota1,gota2,gota3,gota4,gota5,gota6,gota7,gota8,gota9,
	gota10,gota11,gota12,gota13,gota14,gota15,gota16,gota17,gota18,gota19,
	gota20,gota21,gota22,gota23,gota24,gota25,gota26,gota27,gota28]

#Dimensiones
numRows = len(mapa)
numColumns = len(mapa[0])

#Window Tittle
pygame.display.set_caption("Roland on the Ropes (Alpha Demo) by Fernando Paniagua")

#Parpadeo time
ini = pygame.time.get_ticks() #parpadeo de lamparas y llave 
iniGota = pygame.time.get_ticks() #parpadeo de gotas

#Indicador de posesion de llave
hasKey = False

#Determinamos si hay Gamepad
hayJoystick=False
if pygame.joystick.get_count()>0:
	hayJoystick=True
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	if (joystick.get_numaxes()==0):
		hayJoystick=False
	else:
		print ("Joystick detected!")
		print (joystick.get_name())


while True:
	#Ritmo del juego
	reloj.tick(60)

	#Background color - Clear window
	window.fill((0,0,0))

	if estado_juego==2:
		#Fila en la que esta actualmente Roland
		currentRow=int((ry+deltaY+alto_bloque)/alto_bloque)
		
		#Calcula los bloques que le rodean
		bloqueSiguiente = (int)((rx+deltaX*-1) / ancho_bloque + 1)
		bloqueAnterior = (int)((rx+deltaX*-1) / ancho_bloque)
		bloqueActual = (int)(((rx+deltaX*-1)+(ancho_bloque*0.5)) / ancho_bloque)

		#Si esta en la celda de la llave, la agarra
		if mapa[currentRow][bloqueActual] in llaves:
			mapa[currentRow][bloqueActual]=None
			collect.play()
			hasKey=True

		#El estado lo marca la tecla pulsada (1, derecha; 2, izquierda; 3, subiendo; 4 bajando)
		if estado==1:
			if mapa[currentRow][bloqueSiguiente] not in solidos:
				deltaX-=rolandXSpeed
				deltaStep+=1
				if deltaX*-1+windowWidth>(len(mapa[0])*ancho_bloque):
					deltaX+=rolandXSpeed
				if deltaStep+1>limiteDeltaStep:
					deltaStep=0
					step+=1
					if step>2:
						step=0
						pasos.play()

			else:
				step=0
		elif estado==2:
			if mapa[currentRow][bloqueAnterior] not in solidos:
				deltaX+=rolandXSpeed
				deltaStep+=1
				if deltaX>0:
					deltaX=0
				if deltaStep+1>limiteDeltaStep:
					deltaStep=0;
					step+=1
					if step>5:
						step=3
						pasos.play()
			else:
				step=3
		elif estado==3:
			deltaX = bloqueActual*ancho_bloque*-1+(ancho_bloque*2)-CORRECCION_CUERDA #Correccion 'hardcode' para que agarre la cuerda
			deltaY+=rolandYSpeed
			#Si llega con la cabeza a un ladrillo, se para
			if mapa[int((ry+deltaY+alto_bloque+MARGEN_SEGURIDAD)/alto_bloque)][bloqueActual] in solidos:
				deltaY-=rolandYSpeed
			
			#Si llega al exterior, pero no tiene la llave, se para
			if mapa[int((ry+deltaY+alto_bloque+MARGEN_SEGURIDAD)/alto_bloque)][bloqueActual] == sky and hasKey==False:
				deltaY-=rolandYSpeed
				error.play()	

			deltaStep+=1
			if deltaStep+1>10:
				deltaStep=0
				step+=1
				if step>7:
					step=6
					friction.play()
			#Si llega al exterior, cambia de estado y fin del juego
			if mapa[int((ry+deltaY+alto_bloque+MARGEN_SEGURIDAD)/alto_bloque)-1][bloqueActual]==sky:
				success.play()
				estado=0
				step=0
				deltaStep=9
				
		elif estado==4:
			deltaX = bloqueActual*ancho_bloque*-1+(ancho_bloque*2)-CORRECCION_CUERDA #Correccion 'hardcode' para que agarre la cuerda
			deltaY-=rolandYSpeed
			#Si llega con los pies a un ladrillo, se para
			if mapa[int((ry+deltaY+alto_bloque+MARGEN_SEGURIDAD)/alto_bloque)-1][bloqueActual] in solidos:
				deltaY+=rolandYSpeed
			
			deltaStep+=1
			if deltaY<0:
				deltaY=0
			if deltaStep+1>10:
				deltaStep=0
				step+=1
				if step>7:
					step=6
					friction.play()
		
		#Dibuja el mapa
		col=0
		for row in range(0, len(mapa)):
			for elemento in mapa[row]:
				now = pygame.time.get_ticks()
				nowGota = pygame.time.get_ticks()
				if (now>ini+TIEMPO_PARPADEO):
					for cR in range(0, len(mapa)):
						for index, item in enumerate(mapa[cR]):
							if item==bloqueLampara1:
								mapa[cR][index]=bloqueLampara2
							elif mapa[cR][index]==bloqueLampara2:
								mapa[cR][index]=bloqueLampara1
							elif mapa[cR][index] in llaves:
								nextLlave = llaves.index(mapa[cR][index])+1
								if nextLlave>=len(llaves):
									nextLlave=0
								mapa[cR][index]=llaves[nextLlave]
					ini=now

				if (nowGota>iniGota+tiempo_parpadeo_gota):
					for cR in range(0, len(mapa)):
						for index, item in enumerate(mapa[cR]):
							if mapa[cR][index] in gotas:
								nextGota = gotas.index(mapa[cR][index])+1
								if nextGota>=len(gotas):
									nextGota=0
									tiempo_parpadeo_gota=TIEMPO_PARPADEO_GOTA_PAUSA
								else:
									tiempo_parpadeo_gota=TIEMPO_PARPADEO_GOTA_NORMAL
								mapa[cR][index]=gotas[nextGota]
					iniGota=nowGota
		
				if elemento!=None:
					window.blit(elemento,(ancho_bloque*col+deltaX,windowHeight-(alto_bloque*(row+1))+deltaY))
				col+=1
			col=0
		
		window.blit(roland[step],(rx,ry))

		for event in GAME_EVENTS.get():
			#
			#Captura de pulsaciones
			#
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					if (deltaY%alto_bloque)<16:
						estado=1
						step=0
						deltaStep=limiteDeltaStep-1				
						deltaY=deltaY-(deltaY%alto_bloque)
			
				elif event.key == pygame.K_LEFT:
					if (deltaY%alto_bloque)<16:
						estado=2
						step=3
						deltaStep=limiteDeltaStep-1
						deltaY=deltaY-(deltaY%alto_bloque)
			
				elif event.key == pygame.K_UP:
					currentDeltaX = (int)(bloqueActual*ancho_bloque*-1+(ancho_bloque*2)) #Posicion ideal respecto de la cuerda
					if mapa[currentRow][bloqueActual] in cuerdas or mapa[currentRow][bloqueActual]==salida:
						if abs(currentDeltaX-deltaX)<=CORRECCION_CUERDA:#Cambia de estado si esta cerca de la cuerda
							estado=3
							step=6
							deltaStep=limiteDeltaStep-1

				elif event.key == pygame.K_DOWN:
					currentDeltaX = (int)(bloqueActual*ancho_bloque*-1+(ancho_bloque*2)) #Posicion ideal respecto de la cuerda
					if mapa[currentRow][bloqueActual] in cuerdas or mapa[currentRow][bloqueActual]==salida:
						if abs(currentDeltaX-deltaX)<=CORRECCION_CUERDA:#Cambia de estado si esta cerca de la cuerda
							estado=4
							step=6
							deltaStep=limiteDeltaStep-1
			
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			#
			#SUELTA TECLA
			#
			if event.type ==pygame.KEYUP:
				if event.key == pygame.K_RIGHT and estado==1:
					estado=0
					step=0
				elif event.key == pygame.K_LEFT and estado==2:
					estado=0
					step=3
				elif event.key == pygame.K_UP and estado==3:
					estado=0
					step=6
				elif event.key == pygame.K_DOWN and estado==4:
					estado=0
					step=6
			
			#
			#PULSA GAMEPAD
			#
			if hayJoystick:
				xAxis = joystick.get_axis(0) #derecha, izquierda
				yAxis = joystick.get_axis(1) #arriba, abajo
				if xAxis<0.9 and xAxis>-0.9 and yAxis<0.9 and yAxis>-0.9:
					if estado==1:
						estado=0
						step=0
					elif estado==2:
						estado=0
						step=3
					elif estado==3:
						estado=0
						step=6
					elif estado==4:
						estado=0
						step=6
				elif xAxis>0.9:
					if (deltaY%alto_bloque)<16:
						estado=1
						step=0
						deltaStep=limiteDeltaStep-1				
						deltaY=deltaY-(deltaY%alto_bloque)
				elif xAxis<-0.9:
					if (deltaY%alto_bloque)<16:
						estado=2
						step=3
						deltaStep=limiteDeltaStep-1
						deltaY=deltaY-(deltaY%alto_bloque)
				elif yAxis>0.9:
					currentDeltaX = (int)(bloqueActual*ancho_bloque*-1+(ancho_bloque*2)) #Posicion ideal respecto de la cuerda
					if mapa[currentRow][bloqueActual] in cuerdas or mapa[currentRow][bloqueActual]==salida:
						if abs(currentDeltaX-deltaX)<=CORRECCION_CUERDA:#Cambia de estado si esta cerca de la cuerda
							estado=4
							step=6
							deltaStep=limiteDeltaStep-1
				elif yAxis<-0.9:
					currentDeltaX = (int)(bloqueActual*ancho_bloque*-1+(ancho_bloque*2)) #Posicion ideal respecto de la cuerda
					if mapa[currentRow][bloqueActual] in cuerdas or mapa[currentRow][bloqueActual]==salida:
						if abs(currentDeltaX-deltaX)<=CORRECCION_CUERDA:#Cambia de estado si esta cerca de la cuerda
							estado=3
							step=6
							deltaStep=limiteDeltaStep-1
			
			if event.type == GAME_GLOBALS.QUIT:
				pygame.quit()
				sys.exit()	

	pygame.display.update()
	
	#END OF CODE