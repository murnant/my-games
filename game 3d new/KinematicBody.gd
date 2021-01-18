extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	velocity = Vector3()
	velocity += -global_transform.basis.z * 3.0
	move_and_slide(velocity)
