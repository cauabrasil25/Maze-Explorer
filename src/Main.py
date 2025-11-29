import sys
from src.Controller import Controller


def main():
    controller = Controller()

    while controller.running:
        controller.handle_display()
        controller.handle_input()
        controller.update()
    # final display update using Controller's display handler
    controller.handle_display()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrompido pelo usuário. Saindo.')
        sys.exit(0)
