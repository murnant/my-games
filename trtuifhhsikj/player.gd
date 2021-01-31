extends KinematicBody2D
var velocity = Vector2()
export var speed = 100
func get_input():
	velocity = Vector2()
	if Input.is_action_pressed('right'):
		velocity.x = speed
	if Input.is_action_pressed('left'):
		velocity.x = -speed
	if Input.is_action_pressed('down'):
		velocity.y = speed
	if Input.is_action_pressed('up'):
		velocity.y = -speed
func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity)
func _on_Area2D_body_entered(b):
	b.Break()
