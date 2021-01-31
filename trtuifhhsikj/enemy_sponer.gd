extends Node2D
var ENEMY = preload('enemy.tscn')
var timer = 200
func _physics_process(delta):
	timer -= 1
	if timer <= 0:
		var enemy = ENEMY.instance()
		enemy.global_transform = $Position2D.global_transform
		get_node("/root").add_child(enemy)
		timer = 200
