extends Camera
func _input(event):
	if event.is_action_pressed("control"):
		current = not current
