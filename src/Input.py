class Input:
    """Handle user input from console."""

    # Dispatcher moved to Controller. Keep per-state input helpers below.

    def initInput():
        """Get user input for initialization (if any)."""
        return
    
    def mainMenuInput():
        """Get user input for main menu."""
        choice = input("Select an option (1-4): ")
        return choice
    
    def algorithmMenuInput():
        """Get user input for algorithm menu."""
        choice = input("Select an algorithm (1-6): ")
        return choice
    
    def exitConfirmationInput():
        """Get user input for exit confirmation."""
        choice = input("Are you sure you want to exit? (y/n): ")
        return choice
    
    def showScoresInput():
        """Wait for user to press Enter to return to main menu."""
        input("Press Enter to return to the main menu...")
        return
    
