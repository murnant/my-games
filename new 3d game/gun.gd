extends StaticBody
const BULLET = preload("bullet.tscn")
var timer = 0
func _process(delta):
	timer -= 1
	if Input.is_action_pressed("space") and timer <= 0:
		var bullet = BULLET.instance()
		bullet.global_transform = $Position3D.global_transform
		get_node("/root").add_child(bullet)
		timer = 50
