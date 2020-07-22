from datetime import datetime

def _is_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  else:
    return True

def find_prime_party(birth_years, look_ahead=10):
  """Find the next year when all supplied birth
  years will be celebrating a prime number age

  Parameters:
  birth_years (list): A list of years
  look_ahead (int): How far to look for a prime party

  Returns:
  str: The next year a prime party will occur
  or None
  """
  current_year = datetime.now().year
  prime_years = []

  for birth_year in birth_years:
    prime_years.append(set(filter(lambda year: _is_prime(year-birth_year), range(current_year, current_year+look_ahead))))

  shared_primes = prime_years[0].intersection(*prime_years[1:])

  if shared_primes:
    return str(min(shared_primes))
  else:
    return None

if __name__ == "__main__":
  birth_years = [1981, 1996]

  next_prime = find_prime_party(birth_years, look_ahead=40)

  if next_prime:
    print(f'Your next prime party will be {next_prime}.')
  else:
    print('No prime parties found, sorry about that.')
