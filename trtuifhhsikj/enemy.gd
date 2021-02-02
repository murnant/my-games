extends KinematicBody2D
var velocity = Vector2()
func _physics_process(delta):
	velocity.x = -45
	velocity.y += 10
	move_and_slide(velocity)
func Break():
	#print("346373472")
	queue_free()
func _on_Area2D_body_entered(b):
	velocity.y = -850
	move_and_slide(velocity)
