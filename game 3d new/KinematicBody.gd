extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	velocity = Vector3()
	velocity.z += -1
	move_and_slide(velocity)
