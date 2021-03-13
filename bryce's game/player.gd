extends KinematicBody
var velocity = Vector3()
var air = 0
var speed = 0.1
func _process(delta):
	if Input.is_action_pressed("speed_up"):
		speed += 0.1
	if Input.is_action_pressed("speed_down"):
		speed -= 0.1
	if Input.is_action_pressed('right'):
		rotate_y(-0.01)
	if Input.is_action_pressed('left'):
		rotate_y(0.01)
	if Input.is_action_pressed('q'):
		$t/t.rotate_z(0.01)
	if Input.is_action_pressed('e'):
		$t/t.rotate_z(-0.01)
	if Input.is_action_pressed('up'):
		$t.rotate_x(0.01)
	if Input.is_action_pressed('down'):
		$t.rotate_x(-0.01)
	#if Input.is_action_pressed("f_or_j"):
	velocity = $t/t.global_transform.basis.y * speed
	velocity.y += speed
	velocity.y -= air #* 0.01
	#velocity.y = 
	#else:
		#velocity = Vector3()
	move_and_slide(velocity)
	air += velocity.y -speed
