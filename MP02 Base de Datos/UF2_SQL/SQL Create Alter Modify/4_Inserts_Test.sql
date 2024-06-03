use zelda;

insert into game(game_id,user_name,hearts_remaining,blood_moon_countdown,blood_moon_appearances,region) values
(0,'Link',4,5,6,'Hyrule'),
(1,'Paco',5,6,7,'Gerudo');

insert into game_food(game_id,food_name,quantity_remaining) values
(0,'Vegetables',3),
(0,'Fish',5);

insert into game_weapons (game_id,weapon_name,equiped,lives_remaining) values
(0,'Wood Sword',True,3),
(0,'Sword',False,2);

insert into game_enemies (game_id,region,num,xpos,ypos,lifes_remaining) values
(0,'Hyrule', 0, 20, 10, 3),
(0,'Gerudo', 1, 4, 5, 2);

insert into game_sanctuaries_opened (game_id,region,num,xpos,ypos) values
(0,'Hyrule', 0, 40, 7),
(0,'Gerudo', 4, 44, 6);

insert into game_chests_opened (game_id,region,num,xpos,ypos) values
(0, 'Hyrule', 0, 10, 44),
(0, 'Gerudo', 2, 9, 10);






