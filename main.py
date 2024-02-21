from robotina import Game

if __name__ == "__main__":
    mygame = Game(
        title="Robotina",
        tile_size=22,           # Tamaño de cada cuadrícula
        tiles_horizontal=30,    # Cuadrículas horizontales
        tiles_vertical=20,      # Cuadrículas horizontales
    )
    mygame.main()
