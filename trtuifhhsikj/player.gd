extends KinematicBody2D
var velocity = Vector2()
export var speed = 100
var slash = false
var slash_timer = 75
var slash_cooldown = 0
var slash_right = true
func get_input():
	velocity = Vector2()
	velocity.y += 100
	if not slash:
		if Input.is_action_pressed('right'):
			velocity.x = speed
			slash_right = true
			$Sprite2.hide()
		if Input.is_action_pressed('left'):
			velocity.x = -speed
			slash_right = false
			$Sprite2.show()
		if Input.is_action_pressed('down'):
			velocity.y = speed
		
	#slashing code
	if Input.is_action_pressed("space"):
		if slash_cooldown <= 0:
			slash = true
	slash_cooldown -= 1
	if slash_right:
		if slash:
			slash_timer -= 1
			if slash_timer <= 0:
				#slash = false
				if slash_timer >= -73:
					rotate(-0.02)
				else:
					slash = false
					slash_timer = 75
					slash_cooldown = 100
			else:
				rotate(0.02)
	else:
		if slash:
			slash_timer -= 1
			if slash_timer <= 0:
				#slash = false
				if slash_timer >= -73:
					rotate(0.02)
				else:
					slash = false
					slash_timer = 75
					slash_cooldown = 100
			else:
				rotate(-0.02)
func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity)


func _on_Area2D_body_entered(b):
	if slash:
		b.Break()
	else:
		queue_free()
		
		
func _on_jump_body_entered(b):
	#if Input.is_action_pressed('up'):
	velocity.y = -5000
	velocity = move_and_slide(velocity)
	
	
	
	

