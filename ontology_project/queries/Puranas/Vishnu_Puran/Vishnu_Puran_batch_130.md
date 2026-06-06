# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.2581)
- **Original**: जिनमें यह सम्पूर्ण विश्व ओतप्रोत है वे अक्षर, अव्यय और सबके आधारभूत हरि मुझपर प्रसन्न हों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2582)
- **Original**: 3 जिनमें सब कुछ स्थित है, जिनसे सब उत्पन्न हुआ है और जो स्वये सब कुछ तथा सबके आधार हैं, उन श्रीविष्णु- भगवानक्यें नमस्कार है, उन्हें बारम्बार नमस्कार है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2583)
- **Original**: भगवान्‌ अनन्त सर्वगामी हैं; अतः वे ही मेरे रूपसे स्थित है, इसलिये यह साप्पूर्ण जगत्‌ मुझहीसे हुआ है, मैं ही यह सब कुछ हुँ और मुझ सनातनमें ही यह सबब स्थित है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2584)
- **Original**: मैं ही अक्षय, नित्य और आत्माधार परमात्मा हूँ; तथा मैं हो जगत्के आदि और अन्तमें स्थित क्रह्मसंज्षक परमपुरुष हूँ 86
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2585)
- **Original**: न औ की इति श्रीविष्णुपुराणे प्रथमेंडशे एकोनर्विशतितमो5ध्याय:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2586)
- **Original**: 20000 नृहि' 00000»
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2587)
- **Original**: आ020) है बीसवाँ अध्याय अ्रद्वावकृत भगवत्‌-स्तुति और भगवानका आविभाष अ्रीपराशर उकाच एवं सश्लिन्तयन्धिष्णुमभेदेनात्मनो द्विज। तन्मयत्वमबाप्याग्र्य॑ मेने चात्मानमच्युतम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2588)
- **Original**: 9 विसस्मार तथात्पानं नान्यत्किझ्लिदजानत । अहमेवाव्ययो अनन्‍्तः परमात्म्रेत्यचिन्तयत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2589)
- **Original**: 2 तस्य तंद्धावनायोगात्क्षीणपापस्थ वै क्रमात्‌ । शुद्धेउन्तःकरणे विष्णुस्तस्थौ ज्ञानमयोउच्युतः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2590)
- **Original**: 3 योगप्रभावात्यद्रादे जाते विष्णुमयेउसुरे। चलत्युरगबन्यैस्तैमैत्रिय श्रुटित क्षणात्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2591)
- **Original**: 4 भ्रान्तग्राहगण: सोर्मि्ययौ क्षोभ॑ महार्णव: । चतच्नाल चा मही सर्वा सशौलृवनकानना
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2592)
- **Original**: 5 स॒ च त॑ं शैलसब्जातं दैत्यैन्यस्तमथोपारि। उत्क्षिप्य तस्मात्सलिलान्निश्चक्राम महामति: 6 दशा च स जगद्भूयो गगनाद्मुपलक्षणम्‌। प्रद्डादो उस्मीति सस्मार पुनरात्पानमात्मनि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2593)
- **Original**: 7 तुष्टाव च पुनर्थोमाननादि पुरुषोत्तमम्‌। एकाग्रमतिरव्यग्रो.. यतवाक्कायमानस:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2594)
- **Original**: 8 अह्वाद ज्याच 39 नमः परमार्थार्थ स्थूलसूक्ष्म क्षराक्षर व्यक्ताव्यक्त कछातीत सकलेश निरझन
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2595)
- **Original**: 9 करालसौम्यरूपात्मन्विद्याउविद्यामयाच्युत । सदसदृप्सद्वाथ सदसद्धावभावन
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2596)
- **Original**: 119 नित्यानित्यप्रपन्षात्मन्निष्प्रशज्ञामलाश्रित । एकानेक नमस्तुभ्य॑ वासुदेवादिकारण
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2597)
- **Original**: 12 .. ययः सर्वभूतो न च्ञ सर्वभूत:। श्रीपराज्षरजी योले--हे द्विज ! इस प्रकार भगवान्‌ विष्णुको अपनेसे अभिन्न चिन्तन करते-करते पूर्ण तन्‍्मयता प्राप्त हो जानेसे उन्होंने अपनेकों अच्युत रूप ही अनुभव किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2598)
- **Original**: वे अपने-आपको भूल गये; उस समय उन्हें श्रीविष्णुभगवान्‌के अतिरिक्त और कुछ भी प्रतीत न होता था । यस, फेवल यही भावना चित्तमें थी कि मैं ही अव्यय और अनन्त परमात्मा हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2599)
- **Original**: उस भावनाके योगसे ये क्षीण-पाप हो गये और उनके झुद्ध अन्तःकरणमें ज्ञानस्वरूप अच्युत श्रीयिष्णुभगयान्‌ विराजमान हुए
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2600)
- **Original**: है सैत्रेय ! इस प्रकार योगबलसे असुर प्रद्धादजीके विष्णुम्य हो जानेपर उनके विचल्ित होनेसे वे नागपाद्ा एक्र क्षणभरमें ही टूट गये
- **Translation**: 

---

