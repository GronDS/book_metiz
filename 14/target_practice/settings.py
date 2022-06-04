class Settings():
    
    def __init__(self) :
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (233, 244, 252)
        
        self.ship_speed = 1
        self.miss_limit = 2
        
        self.target_speed = 1
        self.target_drop_speed = 5
        self.target_direction = 1
        self.target_color = (0, 0, 0)
        self.target_width = 5
        self.target_height = 200
        
        self.arrow_speed = 2
        self.arrow_width = 40
        self.arrow_height = 3
        self.arrow_color = (0, 0, 0)
        self.arrow_allowed = 3
        
        self.speedup_scale = 1.1
        
    def _reset_difficulty(self):
        self.ship_speed = 1
        self.arrow_speed = 2
        self.target_speed = 1
        
    def _increase_difficulty(self):
        self.ship_speed *= self.speedup_scale
        self.arrow_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale