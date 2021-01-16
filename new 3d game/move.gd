extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	velocity = global_transform.basis.z * delta
	velocity.y = 0.0
	velocity.x = 0.0
	move_and_slide(velocity)
