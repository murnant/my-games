extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	#velocity = global_transform.basis.z / global_transform.basis.z * 9
	velocity += -transform.basis.z *0.000000000000000000000000000000000000000001
	move_and_slide(velocity)
