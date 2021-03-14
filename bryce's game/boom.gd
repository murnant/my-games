extends KinematicBody
var velocity = Vector3()
func _physics_process(delta):
	velocity = Vector3()
	velocity += -global_transform.basis.z * 30
	move_and_slide(velocity)


func _on_Area_body_entered(b):
	$Sprite3D.show()
	b.Break()
