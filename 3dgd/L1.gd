extends Spatial
func _process(delta):
	if Input.is_action_pressed('right'):
		$camerahub.rotate_y(0.005)
	if Input.is_action_pressed('left'):
		$camerahub.rotate_y(-0.005)
	if Input.is_action_pressed('up'):
		$camerahub.rotate_x(-0.005)
	if Input.is_action_pressed('down'):
		$camerahub.rotate_x(0.005)
	$sun.rotate_x(0.01)
