extends Spatial
func _process(delta):
	if Input.is_action_pressed('c_up'):
		rotate_x(0.005)
	if Input.is_action_pressed('c_down'):
		rotate_x(-0.005)
