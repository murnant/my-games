extends Node2D
func _physics_process(delta):
	if Input.is_action_pressed('down'):
		rotate(-0.02)
	if Input.is_action_pressed('up'):
		rotate(0.02)
