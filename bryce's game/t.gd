extends KinematicBody
var velocity = Vector3()
const BULLET = preload("bullet.tscn")
const BOOM = preload("boom.tscn")
var timer = 0
var timer2 = 0
func _process(delta):
	timer -= 1
	if Input.is_action_pressed("space") and timer <= 0:
		var bullet = BULLET.instance()
		bullet.global_transform = $Position3D.global_transform
		get_node("/root").add_child(bullet)
		timer = 3

	timer2 -= 1
	if Input.is_action_pressed("tab") and timer2 <= 0:
		var boom = BOOM.instance()
		boom.global_transform = $Position3D2.global_transform
		get_node("/root").add_child(boom)
		boom = BOOM.instance()
		boom.global_transform = $Position3D3.global_transform
		get_node("/root").add_child(boom)
		timer2 = 50
