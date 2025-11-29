class Input:
    """Handle user input from console."""

    # Dispatcher moved to Controller. Keep per-state input helpers below.

    def initInput():
        """Perform initialization step without waiting for user input.

        This function does not block for input; it can be used by the
        controller to perform any non-interactive initialization actions.
        """
        print('Initializing...')
        return
    
    def welcomeScreenInput():
        """Accept any input at the welcome screen and return it.

        The controller can use the returned value to decide what to do
        next, but most callers will simply ignore the content and
        proceed.
        """
        choice = input()
        return choice
    
    def mainMenuInput():
        """Get user input for main menu."""
        choice = input()
        return choice
    
    def algorithmMenuInput():
        """Get user input for algorithm menu."""
        choice = input()
        return choice
    
    def exitConfirmationInput():
        """Get user input for exit confirmation."""
        choice = input()
        return choice
    
    def showScoresInput():
        """Wait for user to press Enter to return to main menu."""
        input()
        return
    
    def GameScreenInput():
        """Wait for user to press Enter to continue from game screen."""
        input()
        return