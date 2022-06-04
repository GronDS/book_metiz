class Settings():
    """Класс для хранения всех настроек игры Sideways Shooter."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (48, 39, 58)
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (192, 255, 255)
        self.bullet_allowed = 5
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1