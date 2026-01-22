#include <stdbool.h>
#include <string.h>
#include "wordle.h"

bool is_viable_candidate(char *candidate, guess *guesses, int guess_count) {
	// loop over all guesses
	for (int g = 0; g < guess_count; g++) {
		char copy[6];
		strcpy(copy, candidate);

		// Step 1: check EXACT_HIT letters
		for (int i = 0; i < 5; i++) {
			if (guesses[g].feedback[i] == EXACT_HIT) {
				if (copy[i] != guesses[g].letters[i]) {
					return false;
				}
				// cross off this letter
				copy[i] = '_';
			}
		}

		// Step 2: check PARTIAL_HIT letters - same position should not match
		for (int i = 0; i < 5; i++) {
			if (guesses[g].feedback[i] == PARTIAL_HIT) {
				if (candidate[i] == guesses[g].letters[i]) {
					return false;
				}
			}
		}

		// Step 3: check PARTIAL_HIT letters - must exist somewhere else
		for (int i = 0; i < 5; i++) {
			if (guesses[g].feedback[i] == PARTIAL_HIT) {
				bool found = false;
				for (int j = 0; j < 5; j++) {
					if (copy[j] == guesses[g].letters[i]) {
						copy[j] = '_';
						found = true;
						break;
					}
				}
				if (!found) {
					return false;
				}
			}
		}

		// Step 4: check MISS letters - should not exist in candidate
		for (int i = 0; i < 5; i++) {
			if (guesses[g].feedback[i] == MISS) {
				for (int j = 0; j < 5; j++) {
					if (copy[j] == guesses[g].letters[i]) {
						return false;
					}
				}
			}
		}
	}

	return true;
}
