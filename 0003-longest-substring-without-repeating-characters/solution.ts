function lengthOfLongestSubstring(s: string): number {
    const lastSeen: Map<string, number> = new Map()
    let longest = 0
    let start = 0

    for (let i = 0; i < s.length; i++) {
        const char = s[i]
        if (lastSeen.has(char) && lastSeen.get(char)! >= start) {
            start = lastSeen.get(char)! + 1
        }
        lastSeen.set(char, i)
        longest = Math.max(longest, i - start + 1)
    }

    return longest
}
