import turtle

# Initialize the screen
screen = turtle.Screen()
screen.tracer(0)  # Disable automatic screen updates

# Create the snake
snake = [[0, 0], [20, 0], [40, 0]]  # Initial snake segments
pen = turtle.Turtle("square")
pen.penup()

# Draw the initial snake
for segment in snake:
    pen.goto(segment[0], segment[1])
    pen.stamp()

# Function to move the snake
def move_snake():
    pen.clearstamps()  # Clear previous stamps
    new_head = snake[-1].copy()  # Create a new head position
    new_head[0] += 20  # Increment x coordinate
    snake.append(new_head)  # Add new head to the snake
    snake.pop(0)  # Remove the leftmost segment (tail)

    # Draw the updated snake
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()  # Update the screen
    turtle.ontimer(move_snake, 200)  # Move the snake every 200 milliseconds

# Start moving the snake
move_snake()

# Keep the window open
turtle.done()