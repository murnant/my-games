extends "res://bullet.gd"
var timer = 25
var shot = 0
const BULLET = preload("bullet.tscn")
func _physics_process(delta):
	timer -= 1
	if timer <= 0 and shot < 360:
		var bullet = BULLET.instance()
		bullet.global_transform = $Position3D.global_transform
		get_node("/root").add_child(bullet)
		$Position3D.rotate_z(5)
		shot += 5
		
