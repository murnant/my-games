extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	velocity = Vector3()
	velocity += -global_transform.basis.z * 50
	move_and_slide(velocity)
