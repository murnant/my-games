extends Camera
func _input(event):
	if event.is_action_pressed("shift"):
		current = not current
