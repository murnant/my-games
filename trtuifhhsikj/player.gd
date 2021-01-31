extends KinematicBody2D
var velocity = Vector2()
export var speed = 100
var slash = false
var slash_timer = 75
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
	if Input.is_action_pressed("space"):
		slash = true
	if slash:
		slash_timer -= 1
		if slash_timer <= 0:
			#slash = false
			if slash_timer >= -73:
				rotate(-0.01)
			else:
				slash = false
				slash_timer = 75
		else:
			rotate(0.01)
func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity)
func _on_Area2D_body_entered(b):
	if slash:
		b.Break()
