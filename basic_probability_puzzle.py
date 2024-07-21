from fractions import Fraction

# Number of white and black balls in Bag X and Bag Y
white_x = 5
black_x = 4
white_y = 7
black_y = 6

# Total number of balls in Bag X
total_x = white_x + black_x

# Total number of balls in Bag Y
total_y = white_y + black_y

# Probability of drawing a black ball from Bag X
P_Bx = Fraction(black_x, total_x)

# Probability of drawing a white ball from Bag X
P_Wx = Fraction(white_x, total_x)

# Probability of drawing a black ball from Bag Y if a black ball was added from Bag X
P_By_given_Bx = Fraction(black_y + 1, total_y + 1)

# Probability of drawing a black ball from Bag Y if a white ball was added from Bag X
P_By_given_Wx = Fraction(black_y, total_y + 1)

# Total probability of drawing a black ball from Bag Y
P_By = P_Bx * P_By_given_Bx + P_Wx * P_By_given_Wx

# Print the result as an irreducible fraction
print(P_By)
