class GameStats():
  """Track statistics for Alien Invasion."""
  def __init__(self, ai_settings):
    """Initialize statistics."""
    self.ai_settings = ai_settings
    # Start Alien Invasion in an active state.
    self.game_active = True
    self.reset_stats()
  
  def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.ships_left = self.ai_settings.ship_limit