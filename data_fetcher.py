import requests

API_KEY = 'FAv8L5/agkSfDxafl0Fpew==ce3t7X5VNkLcee2E'

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  try:
      name = animal_name
      api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)

      response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

      if response.status_code == requests.codes.ok:
          return response.json()
      else:
          print("Error:", response.status_code, response.text)
          return []

  except Exception as e:
      print(f"An error occurred: {e}.")
      return []