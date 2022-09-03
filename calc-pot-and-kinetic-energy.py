# Python3 program to implement
# the above approach

# Function to calculate Kinetic Energy
def kineticEnergy(M, V):

	# Stores the Kinetic Energy
	KineticEnergy = 0.5 * M * V * V

	return KineticEnergy

# Function to calculate Potential Energy
def potentialEnergy(M, H):

	# Stores the Potential Energy
	PotentialEnergy = M * 9.8 * H

	return PotentialEnergy

# Driver Code
if __name__ == "__main__":

	M = 5.5
	H = 23.5
	V = 10.5

	print("Kinetic Energy = ", kineticEnergy(M, V))
	print("Potential Energy = ", potentialEnergy(M, H))
	
# This code is contributed by AnkThon
