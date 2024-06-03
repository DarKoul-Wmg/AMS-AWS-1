use zelda;

ALTER TABLE game 
	MODIFY game_id INT AUTO_INCREMENT NOT NULL,
    MODIFY user_name VARCHAR(50) NOT NULL,
    MODIFY hearts_remaining INT,
    MODIFY blood_moon_countdown INT,
    MODIFY blood_moon_appearances INT,
    ADD CONSTRAINT game_region CHECK (region IN ("Hyrule","Death_mountain","Gerudo","Necluda","Castle")),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
    MODIFY ganon_dead BOOLEAN DEFAULT 0,  
    ADD CONSTRAINT pk_game PRIMARY KEY (game_id);

    
ALTER TABLE game_food 
	MODIFY food_name VARCHAR(20) NOT NULL,
	ADD CONSTRAINT food_name CHECK (food_name IN("Vegetables","Fish","Meat","Salads","Pescatarian","Roasted")),
    ADD CONSTRAINT pk_game_food PRIMARY KEY (game_id, food_name),
    ADD CONSTRAINT fk_game_game_food FOREIGN KEY (game_id) REFERENCES game(game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW();
    
ALTER TABLE game_weapons
	MODIFY weapon_name VARCHAR(15) NOT NULL,
    ADD CONSTRAINT weapon_name CHECK (weapon_name IN("Wood Sword","Sword","Wood Shield","Shield")),
    MODIFY equiped BOOLEAN DEFAULT false,
    ADD CONSTRAINT pk_game_weapons PRIMARY KEY (game_id, weapon_name),
    ADD CONSTRAINT fk_game_game_weapons FOREIGN KEY (game_id) REFERENCES game(game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW();
    
ALTER TABLE game_enemies 
	MODIFY region VARCHAR(20) NOT NULL,
    MODIFY num INT NOT NULL,
    ADD CONSTRAINT pk_game_enemies PRIMARY KEY (game_id, region, num),
    ADD CONSTRAINT fk_game_game_enemies FOREIGN KEY (game_id) REFERENCES game(game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW();
    
ALTER TABLE game_sanctuaries_opened 
	MODIFY region VARCHAR(20) NOT NULL,
    MODIFY num INT NOT NULL,
    ADD CONSTRAINT pk_game_sanctuaries_opened PRIMARY KEY (game_id, region, num),
    ADD CONSTRAINT fk_game_game_sanctuaries_opened FOREIGN KEY (game_id) REFERENCES game(game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY open BOOLEAN DEFAULT 0,
    MODIFY modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW();

ALTER TABLE game_chests_opened 
	MODIFY region VARCHAR(20) NOT NULL,
    MODIFY num INT NOT NULL,
    ADD CONSTRAINT pk_game_chests_opened PRIMARY KEY (game_id, region, num),
    ADD CONSTRAINT fk_game_game_chests_opened FOREIGN KEY (game_id) REFERENCES game(game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY open BOOLEAN DEFAULT 0,
    MODIFY modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW();
