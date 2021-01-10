extends KinematicBody
var gravity = Vector3.DOWN * 12
var speed = 4
var jump_speed = 1
var spin = 0.1

var velocity = Vector3()

func _physics_process(delta):
	velocity += gravity * delta
	get_imput()
	velocity = move_and_slide(velocity, Vector3.UP)
	
func get_imput():
	velocity.x = 0
	velocity.z = 0
	if Input.is_action_pressed('d'):
		velocity.x += speed
	if Input.is_action_pressed('a'):
		velocity.x -= speed
	if Input.is_action_pressed('s'):
		velocity.z += speed
	if Input.is_action_pressed('w'):
		velocity.z -= speed
		
