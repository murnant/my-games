extends KinematicBody2D
var velocity = Vector2()
func _physics_process(delta):
	velocity.x = -45
	move_and_slide(velocity)
func Break():
	#print("346373472")
	queue_free()
