import requests

word = input("Enter a word: ")
version = "v2"

def get_posts():
    url = f'https://api.dictionaryapi.dev/api/{version}/entries/en/{word}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error: HTTP {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

def display_dictionary(posts):
    if not posts:
        print(f"No data found for '{word}'")
        return
    
    for entry in posts:
        print(f"\nWord: {entry['word'].capitalize()}")
        print("-" * 50)
        
        # Display phonetics
        if entry.get('phonetics'):
            print("Phonetics:")
            for phonetic in entry['phonetics']:
                text = phonetic.get('text', 'N/A')
                audio = phonetic.get('audio', '')
                if audio:
                    print(f"  - {text} (Audio: {audio})")
                else:
                    print(f"  - {text}")
        
        # Display meanings
        if entry.get('meanings'):
            print("\nMeanings:")
            for meaning in entry['meanings']:
                part_of_speech = meaning.get('partOfSpeech', 'N/A').capitalize()
                print(f"  {part_of_speech}:")
                for definition in meaning.get('definitions', []):
                    print(f"    - Definition: {definition.get('definition', 'N/A')}")
                    if definition.get('example'):
                        print(f"      Example: {definition.get('example')}")
                
                # Display synonyms
                if meaning.get('synonyms'):
                    print(f"    Synonyms: {', '.join(meaning['synonyms'])}")
                
                # Display antonyms
                if meaning.get('antonyms'):
                    print(f"    Antonyms: {', '.join(meaning['antonyms'])}")
        
        # Display source and license
        print("\nSource:")
        print(f"  License: {entry['license']['name']} ({entry['license']['url']})")
        print(f"  Source URLs: {', '.join(entry['sourceUrls'])}")

def main():
    posts = get_posts()
    if posts:
        display_dictionary(posts)
    else:
        print(f'Failed to fetch data for "{word}" from API')

if __name__ == '__main__':
    main()