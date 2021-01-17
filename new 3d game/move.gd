extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	#velocity = move_and_slide(velocity, Vector3.UP)
	velocity = Vector3()
	velocity += global_transform.basis.y * 6.0
	velocity += global_transform.basis.x * 6.0
	move_and_slide(velocity)
