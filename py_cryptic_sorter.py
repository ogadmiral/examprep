def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels = "aeiouAEIOU"

    def count_vowels(s: str) -> int:
        count = sum(1 for c in s if c in vowels)
        return count
    
    def skey(s: str):
        return (
            len(s),
            s.lower(),
            count_vowels(s)
        )
    
    result = sorted(strings, key=skey)

    return result

