extends KinematicBody
export var damp = 0.99
onready var active = true
const BULLET = preload("bullet.tscn")
var timer = 0
var velocity = Vector3()
func _process(delta):
	if active:
		if Input.is_action_pressed('right'):
			rotate_y(-0.04)
		if Input.is_action_pressed('left'):
			rotate_y(0.04)
		if Input.is_action_pressed('up'):
			velocity = -global_transform.basis.z * 7
			move_and_slide(velocity)
		if Input.is_action_pressed('down'):
			velocity = global_transform.basis.z * 7
		
		
		if Input.is_action_pressed("space") and timer <= 0:
			var bullet = BULLET.instance()
			bullet.global_transform = $Position3D.global_transform
			get_node("/root").add_child(bullet)
			timer = 50
		
		
	timer -= 1
	velocity *= damp
	move_and_slide(velocity)
