class GameStats():
  """Track statistics for Alien Invasion."""
  def __init__(self, ai_settings):
    """Initialize statistics."""
    # High score should never be reset.
    self.high_score = 0
    self.ai_settings = ai_settings
    # Start Alien Invasion in an inactive state.
    self.game_active = False
    self.reset_stats()
  
  def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.score = 0
    self.level = 1
    self.ships_left = self.ai_settings.ship_limit