extends KinematicBody2D
var velocity = Vector2()
export var speed = 100
var WALL = preload('wall.tscn')
func _input(e):
	# Mouse in viewport coordinates.
	if e is InputEventMouseButton and e.pressed:
		print(get_viewport().get_mouse_position())
		var wall = WALL.instance()
		wall.position = get_viewport().get_mouse_position()
		get_node("/root").add_child(wall)
func get_input():
	if Input.is_action_pressed('right'):
		velocity.x = speed
	if Input.is_action_pressed('left'):
		velocity.x = -speed
	if Input.is_action_pressed('down'):
		velocity.y = speed
	if Input.is_action_pressed('up'):
		velocity.y = -speed
	if Input.is_action_pressed("space"):
		var wall = WALL.instance()
		wall.global_transform = $Position2D.global_transform
		get_node("/root").add_child(wall)
func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity)
