extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	velocity = Vector3()
	#velocity += global_transform.basis.y * 6.0
	velocity += -global_transform.basis.z * 6.0
	move_and_slide(velocity)
