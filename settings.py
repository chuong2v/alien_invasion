class Settings():
  """A class to store all settings for Alien Invasion."""
  def __init__(self):
    """Initialize the game's settings."""
    # Screen settings
    self.screen_width = 1200
    self.screen_height = 600
    self.bg_color = (80, 80, 230)
    self.ship_speed_factor = 1.5
    self.ship_limit = 3

    # Bullet settings
    self.bullet_speed_factor = 1
    self.bullet_width = 2
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 10

    self.alien_speed_factor = 1
    self.fleet_drop_speed = 60
    # fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1