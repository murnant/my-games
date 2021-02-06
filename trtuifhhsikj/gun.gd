extends Node2D
var timer = 0
const BULLET = preload("bullet.tscn")
func _physics_process(delta):
	if Input.is_action_pressed('down'):
		rotate(0.02)
	if Input.is_action_pressed('up'):
		rotate(-0.02)
	timer -= 1
	if Input.is_action_pressed("space") and timer <= 0:
		var bullet = BULLET.instance()
		bullet.global_transform = $Position2D.global_transform
		get_node("/root").add_child(bullet)
		timer = 50
