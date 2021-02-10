extends KinematicBody
var velocity = Vector3()
var gravity = Vector3.DOWN * 12
var speed = 4
var jump_speed = 1
var spin = 0.1

func _physics_process(delta):
	velocity += gravity * delta
	get_imput()
	velocity = move_and_slide(velocity, Vector3.UP)
func get_imput():
	var vy = velocity.y
	velocity = Vector3()
	velocity.y = vy
	if Input.is_action_pressed('right'):
		rotate_y(-0.01)
	if Input.is_action_pressed('left'):
		rotate_y(0.01)
	if Input.is_action_pressed('up'):
		$c.rotate_x(0.01)
	if Input.is_action_pressed('down'):
		$c.rotate_x(-0.01)
	if Input.is_action_pressed("f_or_j"):
		velocity = -global_transform.basis.z * 7
		velocity.y = vy
		move_and_slide(velocity)
