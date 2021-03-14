extends KinematicBody
var velocity = Vector3()
const BULLET = preload("bullet.tscn")
const BOOM = preload("boom.tscn")
var timer = 0
var timer2 = 0
func _process(delta):
	timer -= 1
	if timer <= 0:
		var bullet = BULLET.instance()
		bullet.global_transform = $Position3D.global_transform
		get_node("/root").add_child(bullet)
		timer = 25


func _on_Area_body_entered(body):
	queue_free()
