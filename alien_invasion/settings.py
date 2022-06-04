class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (48, 39, 58)
        
        # Ship settings
        self.ship_limit = 3
        
        # Alien settings
        self.fleet_drop_speed = 10        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (192, 255, 255)
        self.bullet_allowed = 5
        
         # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.easy_scale = 1.0
        self.normal_scale = 1.2
        self.hard_scale = 1.4
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.2
        
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.speedup_scale)

    def normal_level(self):
        self.ship_speed *= self.normal_scale
        self.bullet_speed *= self.normal_scale
        self.alien_speed *= self.normal_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)

    def hard_level(self):
        self.ship_speed *= self.hard_scale
        self.bullet_speed *= self.hard_scale
        self.alien_speed *= self.hard_scale
        
        self.alien_points = int(self.alien_points * self.score_scale ** 2)
