def palindrome():
	

	chaine = list('radar')

	taille = len(chaine) - 1
	i = 0

	tempo = []
	while i < taille:
		if chaine[i] != chaine[taille]:
			return False
		else :
			tempo.append(chaine[i])
			i = i + 1
			taille = taille - 1
			
	return tempo

def palindromeR(mot):
	if len(mot) <= 1:
		return True
	elif (mot[0] == mot[-1]):
		return palindromeR(mot[1:-1])
	else :
		return False


print(palindromeR('radar'))