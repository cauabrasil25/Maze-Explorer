class Input:
    """Handle user input from console."""

    def MainswitchInput(estate):
        switcher = {
            'INIT': Input.MainMenuInput,
            'MAIN_MENU': Input.MainMenuInput,
            'SET_ALGORITHM': Input.AlgorithmMenuInput,
            'EXIT': Input.ExitConfirmationInput,
            'VIEW_SCORES': Input.ShowScoresInput
        }
    
    def MainMenuInput():
        """Get user input for main menu."""
        choice = input("Select an option (1-4): ")
        return choice
    
    def AlgorithmMenuInput():
        """Get user input for algorithm menu."""
        choice = input("Select an algorithm (1-6): ")
        return choice
    
    def ExitConfirmationInput():
        """Get user input for exit confirmation."""
        choice = input("Are you sure you want to exit? (y/n): ")
        return choice
    
    def ShowScoresInput():
        """Wait for user to press Enter to return to main menu."""
        input("Press Enter to return to the main menu...")
        return
    
