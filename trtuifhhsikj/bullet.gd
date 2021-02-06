extends KinematicBody2D
var velocity = Vector2()
func _physics_process(delta):
	velocity = Vector2()
	velocity += global_transform.x * 100.0
	move_and_slide(velocity)
