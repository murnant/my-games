extends StaticBody
const BULLET = preload("bullet.tscn")
func _process(delta):
	if Input.is_action_pressed("space"):
		var bullet = BULLET.instance()
		bullet.global_transform = $Position3D.global_transform
		get_node("/root").add_child(bullet)
