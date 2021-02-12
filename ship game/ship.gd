extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
		move_and_slide(velocity)


func _on_Area_body_entered(body):
	velocity = -global_transform.basis.z * 7


func _on_Area_body_exited(body):
	velocity = Vector3()
