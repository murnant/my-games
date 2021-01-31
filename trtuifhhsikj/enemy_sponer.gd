extends Node2D
var ENEMY = preload('enemy.tscn')
func _physics_process(delta):
	var enemy = ENEMY.instance()
	enemy.global_transform = $Position2D.global_transform
	get_node("/root").add_child(enemy)
